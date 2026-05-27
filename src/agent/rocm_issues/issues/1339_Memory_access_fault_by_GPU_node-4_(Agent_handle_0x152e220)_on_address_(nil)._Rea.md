# Memory access fault by GPU node-4 (Agent handle: 0x152e220) on address (nil). Reason: Page not present or supervisor privilege.

> **Issue #1339**
> **状态**: closed
> **创建时间**: 2020-12-16T11:13:44Z
> **更新时间**: 2021-05-23T01:00:23Z
> **关闭时间**: 2021-02-02T09:56:21Z
> **作者**: bearwithdog
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1339

## 描述

Environment:
rocm-3.9
centos 7.6.8
Issue:
My program submit an error which just like "Memory access fault by GPU node-4 (Agent handle: 0x152e220) on address (nil). Reason: Page not present or supervisor privilege.". 
However,the error has gone,when i add "printf" in device function .  Why does this happened? 
No error code as follows 
```C++
__device__ int cuda_dfs_match(const int len, const unsigned char *str, const int sequence_type, unsigned int *widths, unsigned char *bids, const barracuda_gap_opt_t *opt, alignment_store_t *aln, int best_score, const int max_aln,uint4 * bwt_occ_array,uint4 * rbwt_occ_array)
{
....

printf(" debug_1666 ");

....
}
```
I guess that "printf" makes the threads synchronize. 
Thanks

---

## 评论 (15 条)

### 评论 #1 — ROCmSupport (2020-12-18T04:03:53Z)

Hi @bearwithdog 
Thanks for reaching out.
Can you please help us with more information about the function.
And also share Asic, OS, kernel details too.
Thank you.

---

### 评论 #2 — bearwithdog (2020-12-22T03:21:15Z)

Hi @ROCmSupport  
Thanks for your reply
GPU computing architecture：gfx906  
Rocm version:3.9  
OS:centos-7.6.8
<details>
  <summary>kernel function</summary>
  <pre><code> 
 __global__ void cuda_inexact_match_caller(int no_of_sequences, unsigned short max_sequence_length, alignment_store_t* global_alignment_store, unsigned char cuda_opt,unsigned int *sequences_array,uint4 * bwt_occ_array,uint4 * rbwt_occ_array,uint2 * sequences_index_array)
//CUDA kernal for inexact match on both strands
//calls bwt_cuda_device_calculate_width to determine the boundaries of the search space
//and then calls dfs_match to search for alignment using dfs approach
{
	// Block ID for CUDA threads, as there is only 1 thread per block possible for now
	unsigned int blockId = blockIdx.x * blockDim.x + threadIdx.x;

	//Local store for sequence widths bids and alignments
	unsigned int local_sequence_widths[MAX_SEQUENCE_LENGTH];
	unsigned char local_sequence_bids[MAX_SEQUENCE_LENGTH];
	unsigned char local_sequence[MAX_SEQUENCE_LENGTH];
	unsigned char local_rc_sequence[MAX_SEQUENCE_LENGTH];
	alignment_store_t local_alignment_store;

	//fetch the alignment store from memory
	local_alignment_store = global_alignment_store[blockId];


	int max_aln = options_cuda.max_aln;
	//initialize local options for each query sequence
	barracuda_gap_opt_t local_options = options_cuda;

	//Core function
	// work on valid sequence only
	if ( blockId < no_of_sequences )
	{
		//get sequences from texture memory
		//const uint2 sequence_info = tex1Dfetch(sequences_index_array, local_alignment_store.sequence_id);
	        const uint2 sequence_info = sequences_index_array[local_alignment_store.sequence_id];
		local_alignment_store.finished = 1; //only one run for simple kernel
		const unsigned int sequence_offset = sequence_info.x;
		const unsigned short sequence_length = sequence_info.y;
		unsigned int last_read = ~0;
		unsigned int last_read_data;

		for (int i = 0; i < sequence_length; ++i)
		{
			unsigned char c = read_char(sequence_offset + i, &last_read, &last_read_data,sequences_array);
			local_sequence[i] = c;
			if (local_options.mode & BWA_MODE_COMPREAD)
			{
				local_rc_sequence[i] = (c > 3)? c : (3 - c);
			}else
			{
				local_rc_sequence[i] = c;
			}
		}

		//initialize local options
		if (options_cuda.fnr > 0.0) local_options.max_diff = bwa_cuda_cal_maxdiff(sequence_length, BWA_AVG_ERR, options_cuda.fnr);
		if (local_options.max_diff < options_cuda.max_gapo) local_options.max_gapo = local_options.max_diff;
		//the worst score is lowered from +1 (bwa) to +0 to tighten the search space esp. for long reads
		int worst_score = aln_score2(local_options.max_diff, local_options.max_gapo, local_options.max_gape, local_options);

		//test if there is too many Ns, if true, skip everything and return 0 number of alignments.

		int N = 0;
		for (int i = 0 ; i < sequence_length; ++i)
		{

			if (local_sequence[i] > 3) ++N;
			if (N > local_options.max_diff)
			{
				global_alignment_store[blockId].no_of_alignments = 0;
				return;
			}
		}

		//work on main sequence, i.e. reverse sequence (bwt for w, rbwt for match)
		int sequence_type = 0;

		// Calculate w
		//syncthreads();
		__syncthreads();
		bwt_cuda_device_calculate_width(local_sequence, sequence_type, local_sequence_widths, local_sequence_bids, sequence_length,bwt_occ_array,rbwt_occ_array);

		//Align with forward reference sequence
		//syncthreads();
		int best_score = cuda_dfs_match(sequence_length, local_sequence, sequence_type, local_sequence_widths, local_sequence_bids, &local_options, &local_alignment_store, worst_score, max_aln,bwt_occ_array,rbwt_occ_array);

		// copy alignment info to global memory
		#if OUTPUT_ALIGNMENTS == 1
		global_alignment_store[blockId] = local_alignment_store;
		int no_aln = local_alignment_store.no_of_alignments;
		#endif // OUTPUT_ALIGNMENTS == 1


		//work on reverse complementary sequence (rbwt for w, bwt for match)
		sequence_type = 1;

		// Calculate w
		//syncthreads();
		__syncthreads();
		bwt_cuda_device_calculate_width(local_rc_sequence, sequence_type, local_sequence_widths, local_sequence_bids, sequence_length,bwt_occ_array,rbwt_occ_array);

		//Align with reverse reference sequence
		//syncthreads();
		__syncthreads();
		cuda_dfs_match(sequence_length, local_rc_sequence, sequence_type, local_sequence_widths, local_sequence_bids, &local_options, &local_alignment_store, best_score, max_aln,bwt_occ_array,rbwt_occ_array);

		// copy alignment info to global memory
		#if OUTPUT_ALIGNMENTS == 1
		short rc_no_aln = 0;
		while (rc_no_aln <= (max_aln + max_aln - no_aln) && rc_no_aln < local_alignment_store.no_of_alignments)
		{
			global_alignment_store[blockId].alignment_info[no_aln + rc_no_aln] = local_alignment_store.alignment_info[rc_no_aln];
			rc_no_aln++;
		}
		global_alignment_store[blockId].no_of_alignments = local_alignment_store.no_of_alignments + no_aln;
		#endif // OUTPUT_ALIGNMENTS == 1

	}
	return;
}
</code></pre>
</details>

<details>
  <summary>device function</summary>
  <pre><code> 
__device__ int cuda_dfs_match(const int len, const unsigned char *str, const int sequence_type, unsigned int *widths, unsigned char *bids, const barracuda_gap_opt_t *opt, alignment_store_t *aln, int best_score, const int max_aln,uint4 * bwt_occ_array,uint4 * rbwt_occ_array)
//This function tries to find the alignment of the sequence and returns SA coordinates, no. of mismatches, gap openings and extensions
//It uses a depth-first search approach rather than breath-first as the memory available in CUDA is far less than in CPU mode
//The search rooted from the last char [len] of the sequence to the first with the whole bwt as a ref from start
//and recursively narrow down the k(upper) & l(lower) SA boundaries until it reaches the first char [i = 0], if k<=l then a match is found.
{
	//Initialisations
	int best_diff = opt->max_diff + 1;
	int best_cnt = 0;
	const bwt_t * bwt = (sequence_type == 0)? &rbwt_cuda: &bwt_cuda; // rbwt for sequence 0 and bwt for sequence 1;
	const int bwt_type = 1 - sequence_type;
	int current_stage = 0;
	uint4 entries_info[MAX_SEQUENCE_LENGTH];
	uchar4 entries_scores[MAX_SEQUENCE_LENGTH];
	char4 done_push_types[MAX_SEQUENCE_LENGTH];
	int n_aln = 0;
	int loop_count = 0;
	const int max_count = options_cuda.max_entries;

	//Initialise memory stores first in, last out
	cuda_dfs_initialize(entries_info, entries_scores, done_push_types/*, scores*/); //initialize initial entry, current stage set at 0 and done push type = 0

	//push first entry, the first char of the query sequence into memory stores for evaluation
	cuda_dfs_push(entries_info, entries_scores, done_push_types, len, 0, bwt->seq_len, 0, 0, 0, 0, 0, current_stage); //push initial entry to start

#if DEBUG_LEVEL > 6
	printf("initial k:%u, l: %u \n", 0, bwt->seq_len);
#endif

#if DEBUG_LEVEL > 6
	for (int x = 0; x<len; x++) {
		printf(".%d",str[x]);
	}

	// print out the widths and bids
	printf("\n");
	for (int x = 0; x<len; x++) {
		printf("%i,",bids[x]);
	}
	printf("\n");
	for (int x = 0; x<len; x++) {
		printf("%d;",widths[x]);
	}


printf("\n");

printf("max_diff: %d\n", max_diff);

#endif
<font color='red'>printf(" debug_1666 ");</font>
	while(current_stage >= 0)
	{
		int i,j, m;
		int hit_found, allow_diff, allow_M;
		unsigned int k, l;
		char e_n_mm, e_n_gapo, e_n_gape, e_state;
		unsigned int occ;
		loop_count ++;

		int worst_tolerated_score = (options_cuda.mode & BWA_MODE_NONSTOP)? 1000: best_score + options_cuda.s_mm;

		//define break from loop conditions
		if (n_aln == max_aln) {
#if DEBUG_LEVEL > 7
			printf("breaking on n_aln == max_aln\n");
#endif
			break;
		}
		if (best_cnt > options_cuda.max_top2) {
#if DEBUG_LEVEL > 7
			printf("breaking on best_cnt>...\n");
#endif
			break;
		}
		if (loop_count > max_count) {
#if DEBUG_LEVEL > 7
			printf("loop_count > max_count\n");
#endif
			break;

		}

		//put extracted entry into local variables
		k = entries_info[current_stage].x; // SA interval
		l = entries_info[current_stage].y; // SA interval
		i = entries_info[current_stage].z; // length
		e_n_mm = entries_scores[current_stage].x; // no of mismatches
		e_n_gapo = entries_scores[current_stage].y; // no of gap openings
		e_n_gape = entries_scores[current_stage].z; // no of gap extensions
		e_state = entries_scores[current_stage].w; // state (M/I/D)

		//calculate score
		int score = e_n_mm * options_cuda.s_mm + e_n_gapo * options_cuda.s_gapo + e_n_gape * options_cuda.s_gape;

		//seeding diff
		int max_diff = ((len-i) <  opt->seed_len)? opt->max_seed_diff : opt->max_diff;
//		int max_diff= opt->max_diff;

		//calculate the allowance for differences
		m = max_diff - e_n_mm - e_n_gapo;

#if DEBUG_LEVEL > 7
		printf("k:%u, l: %u, i: %i, score: %d, cur.stage: %d, mm: %d, go: %d, ge: %d, m: %d\n", k, l,i, score, current_stage, e_n_mm, e_n_gapo, e_n_gape, m);
#endif


		if (options_cuda.mode & BWA_MODE_GAPE) m -= e_n_gape;

		if(score > worst_tolerated_score) break;

		// check if the entry is outside boundary or is over the max diff allowed)
		if (m < 0 || (i > 0 && m < bids[i-1]))
		{
#if DEBUG_LEVEL > 6
			printf("breaking: %d, m:%d\n", bids[i-1],m);
#endif
			current_stage --;
			continue;
		}

		// check whether a hit (full sequence when it reaches the last char, i.e. i = 0) is found, if it is, record the alignment information
		hit_found = 0;
		if (!i)
		{
			hit_found = 1;
		}else if (!m) // alternatively if no difference is allowed, just do exact match)
		{
			if ((e_state == STATE_M ||(options_cuda.mode&BWA_MODE_GAPE) || e_n_gape == opt->max_gape))
			{
				if (bwt_cuda_match_exact(bwt_type, i, str, &k, &l,bwt_occ_array,rbwt_occ_array))
				{
					hit_found = 1;
				}else
				{
					current_stage --;
					continue; // if there is no hit, then go backwards to parent stage
				}
			}
		}
		if (hit_found)
		{
			// action for found hits
			//int do_add = 1;

			if (score < best_score)
			{
				best_score = score;
				best_diff = e_n_mm + e_n_gapo + (options_cuda.mode & BWA_MODE_GAPE) * e_n_gape;
				best_cnt = 0; //reset best cnt if new score is better
				if (!(options_cuda.mode & BWA_MODE_NONSTOP))
					max_diff = (best_diff + 1 > opt->max_diff)? opt->max_diff : best_diff + 1; // top2 behaviour
			}
			if (score == best_score) best_cnt += l - k + 1;

			if (e_n_gapo)
			{ // check whether the hit has been found. this may happen when a gap occurs in a tandem repeat
				// if this alignment was already found, do not add to alignment record array unless the new score is better.
				for (j = 0; j < n_aln; ++j)
					if (aln->alignment_info[j].k == k && aln->alignment_info[j].l == l) break;
				if (j < n_aln)
				{
					if (score < aln->alignment_info[j].score)
						{
							aln->alignment_info[j].score = score;
							aln->alignment_info[j].n_mm = e_n_mm;
							aln->alignment_info[j].n_gapo = e_n_gapo;
							aln->alignment_info[j].n_gape = e_n_gape;
						}
					//do_add = 0;
					hit_found = 0;
				}
			}

			if (hit_found)
			{ // append result the alignment record array
				gap_stack_shadow_cuda(l - k + 1, len, bwt->seq_len, entries_info[current_stage].w, widths, bids);
					// record down number of mismatch, gap open, gap extension and a??

					aln->alignment_info[n_aln].n_mm = entries_scores[current_stage].x;
					aln->alignment_info[n_aln].n_gapo = entries_scores[current_stage].y;
					aln->alignment_info[n_aln].n_gape = entries_scores[current_stage].z;
					aln->alignment_info[n_aln].a = sequence_type;
					// the suffix array interval
					aln->alignment_info[n_aln].k = k;
					aln->alignment_info[n_aln].l = l;
					aln->alignment_info[n_aln].score = score;
#if DEBUG_LEVEL > 8
					printf("alignment added: k:%u, l: %u, i: %i, score: %d, cur.stage: %d, m:%d\n", k, l, i, score, current_stage, m);
#endif

					++n_aln;

			}
			current_stage --;
			continue;
		}

		// proceed and evaluate the next base on sequence
		--i;

		// retrieve Occurrence values and determine all the eligible daughter nodes, done only once at the first instance and skip when it is revisiting the stage
		unsigned int ks[MAX_SEQUENCE_LENGTH][4], ls[MAX_SEQUENCE_LENGTH][4];
		char eligible_cs[MAX_SEQUENCE_LENGTH][5], no_of_eligible_cs=0;

		if(!done_push_types[current_stage].x)
		{
			uint4 cuda_cnt_k = (!sequence_type)? rbwt_cuda_occ4(k-1,rbwt_occ_array): bwt_cuda_occ4(k-1,bwt_occ_array);
			uint4 cuda_cnt_l = (!sequence_type)? rbwt_cuda_occ4(l,rbwt_occ_array): bwt_cuda_occ4(l,bwt_occ_array);
			ks[current_stage][0] = bwt->L2[0] + cuda_cnt_k.x + 1;
			ls[current_stage][0] = bwt->L2[0] + cuda_cnt_l.x;
			ks[current_stage][1] = bwt->L2[1] + cuda_cnt_k.y + 1;
			ls[current_stage][1] = bwt->L2[1] + cuda_cnt_l.y;
			ks[current_stage][2] = bwt->L2[2] + cuda_cnt_k.z + 1;
			ls[current_stage][2] = bwt->L2[2] + cuda_cnt_l.z;
			ks[current_stage][3] = bwt->L2[3] + cuda_cnt_k.w + 1;
			ls[current_stage][3] = bwt->L2[3] + cuda_cnt_l.w;

			if (ks[current_stage][0] <= ls[current_stage][0])
			{
				eligible_cs[current_stage][no_of_eligible_cs++] = 0;
			}
			if (ks[current_stage][1] <= ls[current_stage][1])
			{
				eligible_cs[current_stage][no_of_eligible_cs++] = 1;
			}
			if (ks[current_stage][2] <= ls[current_stage][2])
			{
				eligible_cs[current_stage][no_of_eligible_cs++] = 2;
			}
			if (ks[current_stage][3] <= ls[current_stage][3])
			{
				eligible_cs[current_stage][no_of_eligible_cs++] = 3;
			}
			eligible_cs[current_stage][4] = no_of_eligible_cs;
		}else
		{
			no_of_eligible_cs = eligible_cs[current_stage][4];
		}

		// test whether difference is allowed
		allow_diff = 1;
		allow_M = 1;

		if (i)
		{
			if (bids[i-1] > m -1)
			{
				allow_diff = 0;
			}else if (bids[i-1] == m-1 && bids[i] == m-1 && widths[i-1] == widths[i])
			{
				allow_M = 0;
			}
		}

		//donepushtypes stores information for each stage whether a prospective daughter node has been evaluated or not
		//donepushtypes[current_stage].x  exact match, =0 not done, =1 done
		//donepushtypes[current_stage].y  mismatches, 0 not done, =no of eligible cs with a k<=l done
		//donepushtypes[current_stage].z  deletions, =0 not done, =no of eligible cs with a k<=l done
		//donepushtypes[current_stage].w  insertions match, =0 not done, =1 done
		//.z and .w are shared among gap openings and extensions as they are mutually exclusive


		////////////////////////////////////////////////////////////////////////////////////////////////////////////
		// exact match
		////////////////////////////////////////////////////////////////////////////////////////////////////////////

		//try exact match first
		if (!done_push_types[current_stage].x)
		{
#if DEBUG_LEVEL > 8
			printf("trying exact\n");
#endif
			int c = str[i];
			done_push_types[current_stage].x = 1;
			if (c < 4)
			{
#if DEBUG_LEVEL > 8
				printf("c:%i, i:%i\n",c,i);
				printf("k:%u\n",ks[current_stage][c]);
				printf("l:%u\n",ls[current_stage][c]);
#endif

				if (ks[current_stage][c] <= ls[current_stage][c])
				{
					#if DEBUG_LEVEL > 8
					printf("ex match found\n");
					#endif
					cuda_dfs_push(entries_info, entries_scores, done_push_types, i, ks[current_stage][c], ls[current_stage][c], e_n_mm, e_n_gapo, e_n_gape, STATE_M, 0, current_stage+1);
					current_stage++;
					continue;
				}
			}
		}else if (score == worst_tolerated_score)
		{
			allow_diff = 0;
		}

		if (allow_diff)
		{
		#if DEBUG_LEVEL > 8
			printf("trying inexact...\n");
		#endif
			////////////////////////////////////////////////////////////////////////////////////////////////////////////
			// mismatch
			////////////////////////////////////////////////////////////////////////////////////////////////////////////

			if (done_push_types[current_stage].y < no_of_eligible_cs) //check if done before
			{
				int c = eligible_cs[current_stage][(done_push_types[current_stage].y)];
				done_push_types[current_stage].y++;
				if (allow_M) // daughter node - mismatch
				{
					if (score + options_cuda.s_mm <= worst_tolerated_score) //skip if prospective entry is beyond worst tolerated
					{
						if (c != str[i])
						{
							// TODO is the debug message ok?
							#if DEBUG_LEVEL > 8
							 printf("mismatch confirmed\n");
							#endif
							cuda_dfs_push(entries_info, entries_scores, done_push_types, i, ks[current_stage][c], ls[current_stage][c], e_n_mm + 1, e_n_gapo, e_n_gape, STATE_M, 1, current_stage+1);
							current_stage++;
							continue;
						}else if (done_push_types[current_stage].y < no_of_eligible_cs)
						{
							c = eligible_cs[current_stage][(done_push_types[current_stage].y)];
							done_push_types[current_stage].y++;
							cuda_dfs_push(entries_info, entries_scores, done_push_types, i, ks[current_stage][c], ls[current_stage][c], e_n_mm + 1, e_n_gapo, e_n_gape, STATE_M, 1, current_stage+1);
							current_stage++;
							continue;
						}
					}
				}
			}
				////////////////////////////////////////////////////////////////////////////////////////////////////////////
				// Indels (Insertions/Deletions)
				////////////////////////////////////////////////////////////////////////////////////////////////////////////
				if (!e_state) // daughter node - opening a gap insertion or deletion
				{
					if (score + options_cuda.s_gapo <=worst_tolerated_score) //skip if prospective entry is beyond worst tolerated
					{
						if (e_n_gapo < opt->max_gapo)
						{
							if (!done_push_types[current_stage].w)
							{	//insertions
								done_push_types[current_stage].w = 1;
								//unsigned int tmp = (options_cuda.mode & BWA_MODE_LOGGAP)? (int_log2_cuda(e_n_gape + e_n_gapo))>>1 + 1 : e_n_gapo + e_n_gape; (change 6) 
								unsigned int tmp = (options_cuda.mode & BWA_MODE_LOGGAP)? ((int_log2_cuda(e_n_gape + e_n_gapo))>>1) + 1 : e_n_gapo + e_n_gape;
								if (i >= options_cuda.indel_end_skip + tmp && len - i >= options_cuda.indel_end_skip + tmp)
								{
										current_stage++;
										cuda_dfs_push(entries_info, entries_scores, done_push_types, i, k, l, e_n_mm, e_n_gapo + 1, e_n_gape, STATE_I, 1, current_stage);
										continue;
								}
							}
							else if (done_push_types[current_stage].z < no_of_eligible_cs)  //check if done before
							{	//deletions
								//unsigned int tmp = (options_cuda.mode & BWA_MODE_LOGGAP)? (int_log2_cuda(e_n_gape + e_n_gapo))>>1 + 1 : e_n_gapo + e_n_gape;  (change 6)
							        unsigned int tmp = (options_cuda.mode & BWA_MODE_LOGGAP)? ((int_log2_cuda(e_n_gape + e_n_gapo))>>1) + 1 : e_n_gapo + e_n_gape;
								if (i >= options_cuda.indel_end_skip + tmp && len - i >= options_cuda.indel_end_skip + tmp)
								{
									int c = eligible_cs[current_stage][(done_push_types[current_stage].z)];
									done_push_types[current_stage].z++;
									cuda_dfs_push(entries_info, entries_scores, done_push_types, i + 1, ks[current_stage][c], ls[current_stage][c], e_n_mm, e_n_gapo + 1, e_n_gape, STATE_D, 1, current_stage+1);
									current_stage++; //advance stage number by 1
									continue;
								}
								else
								{
									done_push_types[current_stage].z++;
								}
							}
						}
					}
				}else if (e_state == STATE_I) //daughter node - extend an insertion entry
				{
					if(!done_push_types[current_stage].w)  //check if done before
					{
						done_push_types[current_stage].w = 1;
						if (e_n_gape < opt->max_gape)  //skip if no of gap ext is beyond limit
						{
							if (score + options_cuda.s_gape <=worst_tolerated_score) //skip if prospective entry is beyond worst tolerated
							{
								//unsigned int tmp = (options_cuda.mode & BWA_MODE_LOGGAP)? (int_log2_cuda(e_n_gape + e_n_gapo))>>1 + 1 : e_n_gapo + e_n_gape;    ( change 6)                                              
							        unsigned int tmp = (options_cuda.mode & BWA_MODE_LOGGAP)? ((int_log2_cuda(e_n_gape + e_n_gapo))>>1) + 1 : e_n_gapo + e_n_gape;
								if (i >= options_cuda.indel_end_skip + tmp && len - i >= options_cuda.indel_end_skip + tmp)
								{
									current_stage++; //advance stage number by 1
									cuda_dfs_push(entries_info, entries_scores,  done_push_types, i, k, l, e_n_mm, e_n_gapo, e_n_gape + 1, STATE_I, 1, current_stage);
									continue; //skip the rest and proceed to next stage
								}
							}
						}
					}
				}else if (e_state == STATE_D) //daughter node - extend a deletion entry
				{
					occ = l - k + 1;
					if (done_push_types[current_stage].z < no_of_eligible_cs)  //check if done before
					{
						if (e_n_gape < opt->max_gape) //skip if no of gap ext is beyond limit
						{
							if (score + options_cuda.s_gape <=worst_tolerated_score) //skip if prospective entry is beyond worst tolerated
							{
								if (e_n_gape + e_n_gapo < max_diff || occ < options_cuda.max_del_occ)
								{
									//unsigned int tmp = (options_cuda.mode & BWA_MODE_LOGGAP)? (int_log2_cuda(e_n_gape + e_n_gapo))>>1 + 1 :e_n_gapo + e_n_gape;  (change 6)
								        unsigned int tmp = (options_cuda.mode & BWA_MODE_LOGGAP)? ((int_log2_cuda(e_n_gape + e_n_gapo))>>1) + 1 : e_n_gapo + e_n_gape;

									if (i >= options_cuda.indel_end_skip + tmp && len - i >= options_cuda.indel_end_skip + tmp)
									{
										int c = eligible_cs[current_stage][(done_push_types[current_stage].z)];
										done_push_types[current_stage].z++;
										cuda_dfs_push(entries_info, entries_scores, done_push_types, i + 1, ks[current_stage][c], ls[current_stage][c], e_n_mm, e_n_gapo, e_n_gape + 1, STATE_D, 1, current_stage+1);
										current_stage++; //advance stage number
										continue;
									}
								}
							}
						}
						else
						{
							done_push_types[current_stage].z++;
						}
					}
				} //end else if (e_state == STATE_D)*/

		}//end if (!allow_diff)
		current_stage--;

	} //end do while loop

	aln->no_of_alignments = n_aln;

	return best_score;
}
  </code></pre>
</details>

background of the problem:  
1. The BWA was CUDA application and i had transitioned to HIP.  
2. There was no problem before the program runing on the rocm-2.9 and rocm-3.3. The problem only appeared on rocm-3.9.  
3. It still have the problem when i trying to write "printf(" debug_1666 ")" somewhere else. "printf(" debug_1666 ")" must precede on the while loop.
4. printf(" debug_1666 ") in the device function.   
I'm not sure if this is a program problem.Looking forward to your advice. Thanks a lot.


---

### 评论 #3 — ROCmSupport (2020-12-22T10:51:31Z)

Hi @bearwithdog ,

   Could you kindly share the output of the following:

   1) /opt/rocm/bin/rocminfo
   2) /opt/rocm/bin/rocm-bandwidth-test -t
   3) /opt/rocm/bin/rocm-bandwidth-test

   This shall help us get more info about the system you are working on.
    
   Also, if you could provide the repo for checking the whole code it would be easier for us to experiment & find out the problem.


Thanks

---

### 评论 #4 — bearwithdog (2020-12-25T10:42:01Z)

Hi @ROCmSupport
It would be great if you could help me find the problem.
I had upload my project. (https://github.com/bearwithdog/barracuda_beta_hip) 
Please compile in rocm-3.9.1

The source code of cuda.
https://github.com/lh3/bwa/releases/tag/0.6.2

Besides that,I also use ltrace mode to run my project.I don't know that the information could be helpful.

<details>
  <summary>error</summary>
Barracuda, Version 0.6.2 beta
[aln_core] 20bp reads: max_diff = 2
[aln_core] 38bp reads: max_diff = 3
[aln_core] 64bp reads: max_diff = 4
[aln_core] 93bp reads: max_diff = 5
[aln_core] 124bp reads: max_diff = 6
[aln_core] Running CUDA mode.
libamdhip64.so.3->hsa_init(0, 0x7fff3102e318, 0x2b33a3a5dd90, 0xfa5150 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtOpenKFD(0x2b33a4246338, 0x2b33a460d778, 0xffffffff, 0xfa1b00) = 0
libhsa-runtime64.so.1->hsaKmtGetVersion(0x7fff3102df98, 0, 0, 48)                       = 0
libhsa-runtime64.so.1->hsaKmtReleaseSystemProperties(2, 0x80084b01, 0, -1)              = 0
libhsa-runtime64.so.1->hsaKmtAcquireSystemProperties(0x7fff3102dfa0, 0, 0x2b33abcc2ea0, 0xfa1e00) = 0
libhsa-runtime64.so.1->hsaKmtGetNodeProperties(0, 0x7fff3102e030, 0, 0)                 = 0
libhsa-runtime64.so.1->hsaKmtGetNodeMemoryProperties(0, 1, 0xfa0d80, 4)                 = 0
libhsa-runtime64.so.1->hsaKmtGetNodeCacheProperties(0, 0, 26, 0x10272c0)                = 0
libhsa-runtime64.so.1->hsaKmtGetNodeIoLinkProperties(0, 7, 0x102e1e0, 0x102e1e0)        = 0
libhsa-runtime64.so.1->hsaKmtGetNodeProperties(1, 0x7fff3102e030, 0x2b33a460dfe0, 0)    = 0
libhsa-runtime64.so.1->hsaKmtGetNodeMemoryProperties(1, 1, 0xfa8180, 0)                 = 0
libhsa-runtime64.so.1->hsaKmtGetNodeCacheProperties(1, 16, 26, 0x102eb80)               = 0
libhsa-runtime64.so.1->hsaKmtGetNodeIoLinkProperties(1, 7, 0x1035c90, 0x1035c90)        = 0
libhsa-runtime64.so.1->hsaKmtGetNodeProperties(2, 0x7fff3102e030, 49, 0)                = 0
libhsa-runtime64.so.1->hsaKmtGetNodeMemoryProperties(2, 1, 0xfa8180, 0)                 = 0
libhsa-runtime64.so.1->hsaKmtGetNodeCacheProperties(2, 32, 26, 0x1036610)               = 0
libhsa-runtime64.so.1->hsaKmtGetNodeIoLinkProperties(2, 7, 0x103d760, 0x103d760)        = 0
libhsa-runtime64.so.1->hsaKmtGetNodeProperties(3, 0x7fff3102e030, 33, 0)                = 0
libhsa-runtime64.so.1->hsaKmtGetNodeMemoryProperties(3, 1, 0x103d940, 0x103d940)        = 0
libhsa-runtime64.so.1->hsaKmtGetNodeCacheProperties(3, 48, 26, 0x103e0f0)               = 0
libhsa-runtime64.so.1->hsaKmtGetNodeIoLinkProperties(3, 7, 0x10451e0, 0x10451e0)        = 0
libhsa-runtime64.so.1->hsaKmtGetNodeProperties(4, 0x7fff3102e030, 0x9cd0, 0)            = 0
libhsa-runtime64.so.1->hsaKmtGetNodeIoLinkProperties(4, 7, 0x10451e0, 0x10451e0)        = 0
libhsa-runtime64.so.1->hsaKmtGetNodeProperties(5, 0x7fff3102e030, 0x9cd0, 0)            = 0
libhsa-runtime64.so.1->hsaKmtGetNodeIoLinkProperties(5, 7, 0x1045200, 0x1045200)        = 0
libhsa-runtime64.so.1->hsaKmtGetNodeProperties(6, 0x7fff3102e030, 0x9cb0, 0)            = 0
libhsa-runtime64.so.1->hsaKmtGetNodeIoLinkProperties(6, 7, 0x1045200, 0x1045200)        = 0
libhsa-runtime64.so.1->hsaKmtGetNodeProperties(7, 0x7fff3102e030, 0x9cb0, 0)            = 0
libhsa-runtime64.so.1->hsaKmtGetNodeIoLinkProperties(7, 7, 0x1045200, 0x1045200)        = 0
libhsa-runtime64.so.1->hsaKmtGetNodeProperties(4, 0x7fff3102e030, 0x102e1a0, 0)         = 0
libhsa-runtime64.so.1->hsaKmtGetClockCounters(4, 0x10454e0, 0, 0)                       = 0
libhsa-runtime64.so.1->hsaKmtGetNodeMemoryProperties(4, 5, 0x1045790, 12)               = 0
libhsa-runtime64.so.1->hsaKmtGetNodeCacheProperties(4, 0x80001000, 96, 0x1046400)       = 0
libhsa-runtime64.so.1->hsaKmtGetNodeProperties(5, 0x7fff3102e030, 0x102e1a0, 0)         = 0
libhsa-runtime64.so.1->hsaKmtGetClockCounters(5, 0x1061390, 0, 0)                       = 0
libhsa-runtime64.so.1->hsaKmtGetNodeMemoryProperties(5, 5, 0x1061610, 12)               = 0
libhsa-runtime64.so.1->hsaKmtGetNodeCacheProperties(5, 0x80001040, 96, 0x1062280)       = 0
libhsa-runtime64.so.1->hsaKmtGetNodeProperties(6, 0x7fff3102e030, 0x102e1a0, 0x1045800) = 0
libhsa-runtime64.so.1->hsaKmtGetClockCounters(6, 0x107d240, 0, 0)                       = 0
libhsa-runtime64.so.1->hsaKmtGetNodeMemoryProperties(6, 5, 0x107d490, 12)               = 0
libhsa-runtime64.so.1->hsaKmtGetNodeCacheProperties(6, 0x80001080, 96, 0x107e0c0)       = 0
libhsa-runtime64.so.1->hsaKmtGetNodeProperties(7, 0x7fff3102e030, 0x102e1a0, 0x1045c00) = 0
libhsa-runtime64.so.1->hsaKmtGetClockCounters(7, 0x1099050, 0, 0)                       = 0
libhsa-runtime64.so.1->hsaKmtGetNodeMemoryProperties(7, 5, 0x1099300, 12)               = 0
libhsa-runtime64.so.1->hsaKmtGetNodeCacheProperties(7, 0x800010c0, 96, 0x1099f30)       = 0
libhsa-runtime64.so.1->hsaKmtGetClockCounters(0, 0x7fff3102e1f0, 1, 0x102e100)          = 0
libhsa-runtime64.so.1->hsaKmtCreateEvent(0x7fff3102e1a0, 1, 0, 0x7fff3102e198 <unfinished ...>
libhsakmt.so.1->hsaKmtAllocMemory(0, 0x8000, 4161, 0x7fff3102e0e0)                      = 0
libhsakmt.so.1->hsaKmtMapMemoryToGPU(0x2b33a2f88000, 0x8000, 0x7fff3102e0e8, -1)        = 0
<... hsaKmtCreateEvent resumed> )                                                       = 0
libhsa-runtime64.so.1->hsaKmtAllocMemory(0, 4096, 64, 0x7fff3102e048)                   = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b33a2f83000, 4096, 0x7fff3102e048, 0) = 0
libhsa-runtime64.so.1->hsaKmtCreateEvent(0x7fff3102e0a0, 0, 0, 0x7fff3102e090)          = 0
libhsa-runtime64.so.1->hsaKmtAllocMemory(4, 0x100000000, 576, 0x7fff3102e170)           = 0
libhsa-runtime64.so.1->hsaKmtAllocMemory(0, 8192, 64, 0x7fff3102e138)                   = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b33a2f92000, 8192, 0x7fff3102e138, 0) = 0
libhsa-runtime64.so.1->hsaKmtAllocMemory(0, 4096, 4160, 0x7fff3102dec8)                 = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b33a2f85000, 4096, 0x7fff3102dec8, 0) = 0
libhsa-runtime64.so.1->hsaKmtSetTrapHandler(4, 0x2b33a2f85000, 4096, 0x2b33a2f92000)    = 0
libhsa-runtime64.so.1->hsaKmtAllocMemory(5, 0x100000000, 576, 0x7fff3102e170)           = 0
libhsa-runtime64.so.1->hsaKmtAllocMemory(0, 8192, 64, 0x7fff3102e138)                   = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b33a2f96000, 8192, 0x7fff3102e138, 0) = 0
libhsa-runtime64.so.1->hsaKmtAllocMemory(0, 4096, 4160, 0x7fff3102dec8)                 = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b33a2f99000, 4096, 0x7fff3102dec8, 0) = 0
libhsa-runtime64.so.1->hsaKmtSetTrapHandler(5, 0x2b33a2f99000, 4096, 0x2b33a2f96000)    = 0
libhsa-runtime64.so.1->hsaKmtAllocMemory(6, 0x100000000, 576, 0x7fff3102e170)           = 0
libhsa-runtime64.so.1->hsaKmtAllocMemory(0, 8192, 64, 0x7fff3102e138)                   = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b33a2f9c000, 8192, 0x7fff3102e138, 0) = 0
libhsa-runtime64.so.1->hsaKmtAllocMemory(0, 4096, 4160, 0x7fff3102dec8)                 = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b33a2f9f000, 4096, 0x7fff3102dec8, 0) = 0
libhsa-runtime64.so.1->hsaKmtSetTrapHandler(6, 0x2b33a2f9f000, 4096, 0x2b33a2f9c000)    = 0
libhsa-runtime64.so.1->hsaKmtAllocMemory(7, 0x100000000, 576, 0x7fff3102e170)           = 0
libhsa-runtime64.so.1->hsaKmtAllocMemory(0, 8192, 64, 0x7fff3102e138)                   = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b33a2fa2000, 8192, 0x7fff3102e138, 0) = 0
libhsa-runtime64.so.1->hsaKmtAllocMemory(0, 4096, 4160, 0x7fff3102dec8)                 = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b33a2fa5000, 4096, 0x7fff3102dec8, 0) = 0
libhsa-runtime64.so.1->hsaKmtSetTrapHandler(7, 0x2b33a2fa5000, 4096, 0x2b33a2fa2000)    = 0
<... hsa_init resumed> )                                                                = 0
libamdhip64.so.3->hsa_system_get_major_extension_table(513, 1, 24, 0x2b33a3d26fa0)      = 0
libamdhip64.so.3->hsa_iterate_agents(0x2b33a3a4de20, 0, 0x7fff3102e1b8, 0x2b33a3d26fa8 <unfinished ...>
libamdhip64.so.3->hsa_agent_get_info(0x1026a60, 17, 0x7fff3102e19c, 0x2b33a3d26fa8)     = 0
libamdhip64.so.3->hsa_amd_agent_iterate_memory_pools(0x1026a60, 0x2b33a3a4aa80, 0x7fff3102e1a0, 0x2b33a3d26fa8 <unfinished ...>
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x1026c40, 0, 0x7fff3102e0f8, 0x7fff3102e1a0) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x1026c40, 1, 0x7fff3102e0fc, 0x2b33a4907fb4) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x1026f80, 0, 0x7fff3102e0f8, 0x2b33a4907fb4) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x1026f80, 1, 0x7fff3102e0fc, 0x2b33a4907fb4) = 0
<... hsa_amd_agent_iterate_memory_pools resumed> )                                      = 1
libamdhip64.so.3->hsa_agent_get_info(0x102e1e0, 17, 0x7fff3102e19c, 0)                  = 0
libamdhip64.so.3->hsa_amd_agent_iterate_memory_pools(0x102e1e0, 0x2b33a3a4aa80, 0x7fff3102e1a0, 0 <unfinished ...>
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x102e3c0, 0, 0x7fff3102e0f8, 0x7fff3102e1a0) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x102e3c0, 1, 0x7fff3102e0fc, 0x2b33a4907fb4) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x102e7a0, 0, 0x7fff3102e0f8, 0x2b33a4907fb4) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x102e7a0, 1, 0x7fff3102e0fc, 0x2b33a4907fb4) = 0
<... hsa_amd_agent_iterate_memory_pools resumed> )                                      = 1
libamdhip64.so.3->hsa_agent_get_info(0x1035c90, 17, 0x7fff3102e19c, 0x10b5000)          = 0
libamdhip64.so.3->hsa_amd_agent_iterate_memory_pools(0x1035c90, 0x2b33a3a4aa80, 0x7fff3102e1a0, 0x10b5000 <unfinished ...>
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x1035e70, 0, 0x7fff3102e0f8, 0x7fff3102e1a0) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x1035e70, 1, 0x7fff3102e0fc, 0x2b33a4907fb4) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x1036230, 0, 0x7fff3102e0f8, 0x2b33a4907fb4) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x1036230, 1, 0x7fff3102e0fc, 0x2b33a4907fb4) = 0
<... hsa_amd_agent_iterate_memory_pools resumed> )                                      = 1
libamdhip64.so.3->hsa_agent_get_info(0x103d760, 17, 0x7fff3102e19c, 0x10b6500)          = 0
libamdhip64.so.3->hsa_amd_agent_iterate_memory_pools(0x103d760, 0x2b33a3a4aa80, 0x7fff3102e1a0, 0x10b6500 <unfinished ...>
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x103d970, 0, 0x7fff3102e0f8, 0x7fff3102e1a0) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x103d970, 1, 0x7fff3102e0fc, 0x2b33a4907fb4) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x103dd30, 0, 0x7fff3102e0f8, 0x2b33a4907fb4) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x103dd30, 1, 0x7fff3102e0fc, 0x2b33a4907fb4) = 0
<... hsa_amd_agent_iterate_memory_pools resumed> )                                      = 1
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 17, 0x7fff3102e19c, 0x2b33a4907fb4)     = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 17, 0x7fff3102e19c, 0)                  = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 17, 0x7fff3102e19c, 0x10b5000)          = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 17, 0x7fff3102e19c, 0x10b6900)          = 0
<... hsa_iterate_agents resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 0xa000, 0x7fff3102e2c8, 0x10b6a38)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 0, 0x7fff3102e2d0, 0x10b6a38)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 4, 0x10b7280, 0x2b33a3cd7920)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 0xa010, 0x7fff3102e160, 0x2b33a3cd7920) = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 0xa006, 0x7fff3102e164, 0x10b6020)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 19, 0x7fff3102deb0, 0x10b6020)          = 0
libamdhip64.so.3->hsa_isa_get_info_alt(0xf0f770, 0, 0x7fff3102de98, 0x10b6020)          = 0
libamdhip64.so.3->hsa_isa_get_info_alt(0xf0f770, 1, 0x10b7171, 0x10b6500)               = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 0xa009, 0x7fff3102dee0, 0)              = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 0xa002, 0x10b6cf4, 0)                   = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 0xa001, 0x10b6dfc, 0x10b6a70)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 18, 0x7fff3102dec0, 0x10b6a70)          = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 0xa003, 0x10b6d68, 0x10b74b0)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 0xa008, 0x10b6d6c, 0x10b74b0)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 0xa007, 0x10b7014, 0x10b74b0)           = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x10451e0, 0x1026c40, 1, 0x7fff3102de18) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x10451e0, 0x1026c40, 2, 0x10b6550) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x10451e0, 0x102e3c0, 1, 0x7fff3102de18) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x10451e0, 0x102e3c0, 2, 0x10b74c0) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x10451e0, 0x1035e70, 1, 0x7fff3102de18) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x10451e0, 0x1035e70, 2, 0x10b74c0) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x10451e0, 0x103d970, 1, 0x7fff3102de18) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x10451e0, 0x103d970, 2, 0x10b74c0) = 0
libamdhip64.so.3->hsa_amd_agent_iterate_memory_pools(0x10451e0, 0x2b33a3a4ab10, 0x10b6ca0, 0x2b33a3d22440 <unfinished ...>
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x1045840, 0, 0x7fff3102ddf4, 0x10b6ca0) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x1045840, 1, 0x7fff3102ddf8, 0x2b33a4907fb4) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1026a60, 0x1045840, 0, 0x7fff3102ddfc) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x1045c90, 0, 0x7fff3102ddf4, 4)         = 0
<... hsa_amd_agent_iterate_memory_pools resumed> )                                      = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1061090, 0x1045840, 0, 0x7fff3102df20) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x107cf40, 0x1045840, 0, 0x7fff3102df20) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1098d50, 0x1045840, 0, 0x7fff3102df20) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x1045c90, 2, 0x7fff3102deb8, 0x10b74c0) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x1045840, 2, 0x7fff3102dfa0, 0x2b33a4907fb4) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x1045840, 6, 0x10b72c0, 100)            = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 8, 0x7fff3102de9c, 0x2b33a4907fb4)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 7, 0x7fff3102deaa, 0x2b33a4907fb4)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 21, 0x7fff3102de94, 0)                  = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 22, 0x7fff3102de96, 0)                  = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 20, 0x7fff3102df20, 0x10b6500)          = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 0x300b, 0x10b6dd0, 0)                   = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 0x3009, 0x10b6d80, 0)                   = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 0x300a, 0x10b6d88, 0)                   = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 0x3003, 0x7fff3102ded0, 0 <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x10451e0, 0x3003, 0x7fff3102ded0, 0 <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_agent_iterate_memory_pools(0x1026a60, 0x2b33a48f4730, 0x10b7610, 8) = 1
libhsa-runtime64.so.1->hsaKmtGetTileConfig(4, 0x7fff3102d8a0, 0x7fff3102d870, 6)        = 0
libhsa-runtime64.so.1->hsaKmtGetTileConfig(5, 0x7fff3102d8a0, 0x7fff3102d870, 6)        = 0
libhsa-runtime64.so.1->hsaKmtGetTileConfig(6, 0x7fff3102d8a0, 0x7fff3102d870, 6)        = 0
libhsa-runtime64.so.1->hsaKmtGetTileConfig(7, 0x7fff3102d8a0, 0x7fff3102d870, 6)        = 0
<... hsa_amd_image_get_info_max_dim resumed> )                                          = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 0x3007, 0x7fff3102ded0, 0x7fff3102dbac <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x10451e0, 0x3007, 0x7fff3102ded0, 0x7fff3102dbac) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 0x3008, 0x7fff3102dea4, 0x7fff3102dbac <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x10451e0, 0x3008, 0x7fff3102dea4, 0x7fff3102dbac) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 0x3002, 0x7fff3102ded0, 0x7fff3102dbac <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x10451e0, 0x3002, 0x7fff3102ded0, 0x7fff3102dbac) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 6, 0x10b700c, 0x7fff3102dbac)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 0xa007, 0x10b6d70, 0x7fff3102dbac)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 0xa00a, 0x7fff3102dea0, 0x7fff3102dbac) = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 18, 0x7fff3102ded0, 0x7fff3102dbac)     = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 0xa012, 0x7fff3102dea4, 0x7fff3102dbac) = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x1026f80, 0x101000, 0, 0x7fff3102e088 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(0, 0x101000, 8256, 0x7fff3102dfa8)             = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(4, 0x10b6b00, 0, 0x2b34ac500000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b34ac500000, 0x7fff3102de40, 0, 0x2b33a42cc160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b34ac500000, 0x101000, 0x7fff3102df48, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x1026f80, 0x101000, 0, 0x7fff3102e088 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(0, 0x101000, 8256, 0x7fff3102dfa8)             = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(4, 0x10b6b00, 0, 0x2b34ac700000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b34ac700000, 0x7fff3102de40, 0, 0x2b33a42cc160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b34ac700000, 0x101000, 0x7fff3102df48, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_signal_create(1, 0, 0, 0x10b72b0 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtCreateEvent(0x7fff3102e070, 0, 0, 0x7fff3102e060)          = 0
<... hsa_signal_create resumed> )                                                       = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 0xa000, 0x7fff3102e2c8, 0x10d8448)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 0, 0x7fff3102e2d0, 0x10d8448)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 4, 0x10d82c0, 0x2b33a3cd7920)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 0xa010, 0x7fff3102e160, 0x2b33a3cd7920) = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 0xa006, 0x7fff3102e164, 0x10d84f0)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 19, 0x7fff3102deb0, 0x10d84f0)          = 0
libamdhip64.so.3->hsa_isa_get_info_alt(0xf0f770, 0, 0x7fff3102de98, 0x10d84f0)          = 0
libamdhip64.so.3->hsa_isa_get_info_alt(0xf0f770, 1, 0x10d81b1, 0x10d8700)               = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 0xa009, 0x7fff3102dee0, 0)              = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 0xa002, 0x10d7d34, 0)                   = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 0xa001, 0x10d7e3c, 0x10d78c0)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 18, 0x7fff3102dec0, 0x10d78c0)          = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 0xa003, 0x10d7da8, 0x10d8520)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 0xa008, 0x10d7dac, 0x10d8520)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 0xa007, 0x10d8054, 0x10d8520)           = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1061090, 0x1026c40, 1, 0x7fff3102de18) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1061090, 0x1026c40, 2, 0x10d7870) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1061090, 0x102e3c0, 1, 0x7fff3102de18) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1061090, 0x102e3c0, 2, 0x10d7870) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1061090, 0x1035e70, 1, 0x7fff3102de18) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1061090, 0x1035e70, 2, 0x10d7870) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1061090, 0x103d970, 1, 0x7fff3102de18) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1061090, 0x103d970, 2, 0x10d7870) = 0
libamdhip64.so.3->hsa_amd_agent_iterate_memory_pools(0x1061090, 0x2b33a3a4ab10, 0x10d7ce0, 0x2b33a3d22440 <unfinished ...>
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x10616c0, 0, 0x7fff3102ddf4, 0x10d7ce0) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x10616c0, 1, 0x7fff3102ddf8, 0x2b33a4907fb4) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x102e1e0, 0x10616c0, 0, 0x7fff3102ddfc) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x1061b10, 0, 0x7fff3102ddf4, 5)         = 0
<... hsa_amd_agent_iterate_memory_pools resumed> )                                      = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x10451e0, 0x10616c0, 0, 0x7fff3102df20) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x107cf40, 0x10616c0, 0, 0x7fff3102df20) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1098d50, 0x10616c0, 0, 0x7fff3102df20) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x1061b10, 2, 0x7fff3102deb8, 0x10d7870) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x10616c0, 2, 0x7fff3102dfa0, 0x2b33a4907fb4) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x10616c0, 6, 0x10d8300, 100)            = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 8, 0x7fff3102de9c, 0x2b33a4907fb4)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 7, 0x7fff3102deaa, 0x2b33a4907fb4)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 21, 0x7fff3102de94, 0)                  = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 22, 0x7fff3102de96, 0)                  = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 20, 0x7fff3102df20, 0x10d8500)          = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 0x300b, 0x10d7e10, 0)                   = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 0x3009, 0x10d7dc0, 0)                   = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 0x300a, 0x10d7dc8, 0)                   = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 0x3003, 0x7fff3102ded0, 0 <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x1061090, 0x3003, 0x7fff3102ded0, 0) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 0x3007, 0x7fff3102ded0, 0x7fff3102dbac <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x1061090, 0x3007, 0x7fff3102ded0, 0x7fff3102dbac) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 0x3008, 0x7fff3102dea4, 0x7fff3102dbac <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x1061090, 0x3008, 0x7fff3102dea4, 0x7fff3102dbac) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 0x3002, 0x7fff3102ded0, 0x7fff3102dbac <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x1061090, 0x3002, 0x7fff3102ded0, 0x7fff3102dbac) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 6, 0x10d804c, 0x7fff3102dbac)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 0xa007, 0x10d7db0, 0x7fff3102dbac)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 0xa00a, 0x7fff3102dea0, 0x7fff3102dbac) = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 18, 0x7fff3102ded0, 0x7fff3102dbac)     = 0
libamdhip64.so.3->hsa_agent_get_info(0x1061090, 0xa012, 0x7fff3102dea4, 0x7fff3102dbac) = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x102e7a0, 0x101000, 0, 0x7fff3102e088 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(1, 0x101000, 8256, 0x7fff3102dfa8)             = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(4, 0x10b6b00, 0, 0x2b34ac900000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b34ac900000, 0x7fff3102de40, 0, 0x2b33a42cc160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b34ac900000, 0x101000, 0x7fff3102df48, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x102e7a0, 0x101000, 0, 0x7fff3102e088 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(1, 0x101000, 8256, 0x7fff3102dfa8)             = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(4, 0x10b6b00, 0, 0x2b34acb00000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b34acb00000, 0x7fff3102de40, 0, 0x2b33a42cc160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b34acb00000, 0x101000, 0x7fff3102df48, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_signal_create(1, 0, 0, 0x10d82f0 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtCreateEvent(0x7fff3102e070, 0, 0, 0x7fff3102e060)          = 0
<... hsa_signal_create resumed> )                                                       = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 0xa000, 0x7fff3102e2c8, 0x10d8cf8)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 0, 0x7fff3102e2d0, 0x10d8cf8)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 4, 0x10d96e0, 0x2b33a3cd7920)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 0xa010, 0x7fff3102e160, 0x2b33a3cd7920) = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 0xa006, 0x7fff3102e164, 0)              = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 19, 0x7fff3102deb0, 0)                  = 0
libamdhip64.so.3->hsa_isa_get_info_alt(0xf0f770, 0, 0x7fff3102de98, 0)                  = 0
libamdhip64.so.3->hsa_isa_get_info_alt(0xf0f770, 1, 0x10d95d1, 0x10d9b00)               = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 0xa009, 0x7fff3102dee0, 0)              = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 0xa002, 0x10d9154, 0)                   = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 0xa001, 0x10d925c, 0x10d9800)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 18, 0x7fff3102dec0, 0x10d9800)          = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 0xa003, 0x10d91c8, 0x10d9910)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 0xa008, 0x10d91cc, 0x10d9910)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 0xa007, 0x10d9474, 0x10d9910)           = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x107cf40, 0x1026c40, 1, 0x7fff3102de18) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x107cf40, 0x1026c40, 2, 0x10d98f0) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x107cf40, 0x102e3c0, 1, 0x7fff3102de18) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x107cf40, 0x102e3c0, 2, 0x10d98f0) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x107cf40, 0x1035e70, 1, 0x7fff3102de18) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x107cf40, 0x1035e70, 2, 0x10d98f0) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x107cf40, 0x103d970, 1, 0x7fff3102de18) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x107cf40, 0x103d970, 2, 0x10d98f0) = 0
libamdhip64.so.3->hsa_amd_agent_iterate_memory_pools(0x107cf40, 0x2b33a3a4ab10, 0x10d9100, 0x2b33a3d22440 <unfinished ...>
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x107d540, 0, 0x7fff3102ddf4, 0x10d9100) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x107d540, 1, 0x7fff3102ddf8, 0x2b33a4907fb4) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1035c90, 0x107d540, 0, 0x7fff3102ddfc) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x107d970, 0, 0x7fff3102ddf4, 6)         = 0
<... hsa_amd_agent_iterate_memory_pools resumed> )                                      = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x10451e0, 0x107d540, 0, 0x7fff3102df20) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1061090, 0x107d540, 0, 0x7fff3102df20) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1098d50, 0x107d540, 0, 0x7fff3102df20) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x107d970, 2, 0x7fff3102deb8, 0x10d98f0) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x107d540, 2, 0x7fff3102dfa0, 0x2b33a4907fb4) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x107d540, 6, 0x10d9720, 100)            = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 8, 0x7fff3102de9c, 0x2b33a4907fb4)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 7, 0x7fff3102deaa, 0x2b33a4907fb4)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 21, 0x7fff3102de94, 0)                  = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 22, 0x7fff3102de96, 0)                  = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 20, 0x7fff3102df20, 0x10d9900)          = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 0x300b, 0x10d9230, 0x10d9f50)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 0x3009, 0x10d91e0, 0x10d9f50)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 0x300a, 0x10d91e8, 0x10d9f50)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 0x3003, 0x7fff3102ded0, 0x10d9f50 <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x107cf40, 0x3003, 0x7fff3102ded0, 0x10d9f50) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 0x3007, 0x7fff3102ded0, 0x7fff3102dbac <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x107cf40, 0x3007, 0x7fff3102ded0, 0x7fff3102dbac) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 0x3008, 0x7fff3102dea4, 0x7fff3102dbac <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x107cf40, 0x3008, 0x7fff3102dea4, 0x7fff3102dbac) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 0x3002, 0x7fff3102ded0, 0x7fff3102dbac <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x107cf40, 0x3002, 0x7fff3102ded0, 0x7fff3102dbac) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 6, 0x10d946c, 0x7fff3102dbac)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 0xa007, 0x10d91d0, 0x7fff3102dbac)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 0xa00a, 0x7fff3102dea0, 0x7fff3102dbac) = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 18, 0x7fff3102ded0, 0x7fff3102dbac)     = 0
libamdhip64.so.3->hsa_agent_get_info(0x107cf40, 0xa012, 0x7fff3102dea4, 0x7fff3102dbac) = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x1036230, 0x101000, 0, 0x7fff3102e088 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(2, 0x101000, 8256, 0x7fff3102dfa8)             = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(4, 0x10b6b00, 0, 0x2b34acd00000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b34acd00000, 0x7fff3102de40, 0, 0x2b33a42cc160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b34acd00000, 0x101000, 0x7fff3102df48, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x1036230, 0x101000, 0, 0x7fff3102e088 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(2, 0x101000, 8256, 0x7fff3102dfa8)             = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(4, 0x10b6b00, 0, 0x2b34acf00000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b34acf00000, 0x7fff3102de40, 0, 0x2b33a42cc160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b34acf00000, 0x101000, 0x7fff3102df48, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_signal_create(1, 0, 0, 0x10d9710 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtCreateEvent(0x7fff3102e070, 0, 0, 0x7fff3102e060)          = 0
<... hsa_signal_create resumed> )                                                       = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 0xa000, 0x7fff3102e2c8, 0x10da0e8)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 0, 0x7fff3102e2d0, 0x10da0e8)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 4, 0x10daaa0, 0x2b33a3cd7920)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 0xa010, 0x7fff3102e160, 0x2b33a3cd7920) = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 0xa006, 0x7fff3102e164, 0x10dacb0)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 19, 0x7fff3102deb0, 0x10dacb0)          = 0
libamdhip64.so.3->hsa_isa_get_info_alt(0xf0f770, 0, 0x7fff3102de98, 0x10dacb0)          = 0
libamdhip64.so.3->hsa_isa_get_info_alt(0xf0f770, 1, 0x10da991, 0x10dad00)               = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 0xa009, 0x7fff3102dee0, 0)              = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 0xa002, 0x10da514, 0)                   = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 0xa001, 0x10da61c, 0x10dabc0)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 18, 0x7fff3102dec0, 0x10dabc0)          = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 0xa003, 0x10da588, 0x10dad80)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 0xa008, 0x10da58c, 0x10dad80)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 0xa007, 0x10da834, 0x10dad80)           = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1098d50, 0x1026c40, 1, 0x7fff3102de18) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1098d50, 0x1026c40, 2, 0x10dacf0) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1098d50, 0x102e3c0, 1, 0x7fff3102de18) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1098d50, 0x102e3c0, 2, 0x10dacf0) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1098d50, 0x1035e70, 1, 0x7fff3102de18) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1098d50, 0x1035e70, 2, 0x10dacf0) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1098d50, 0x103d970, 1, 0x7fff3102de18) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1098d50, 0x103d970, 2, 0x10dacf0) = 0
libamdhip64.so.3->hsa_amd_agent_iterate_memory_pools(0x1098d50, 0x2b33a3a4ab10, 0x10da4c0, 0x2b33a3d22440 <unfinished ...>
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x10993b0, 0, 0x7fff3102ddf4, 0x10da4c0) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x10993b0, 1, 0x7fff3102ddf8, 0x2b33a4907fb4) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x103d760, 0x10993b0, 0, 0x7fff3102ddfc) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x10997e0, 0, 0x7fff3102ddf4, 7)         = 0
<... hsa_amd_agent_iterate_memory_pools resumed> )                                      = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x10451e0, 0x10993b0, 0, 0x7fff3102df20) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1061090, 0x10993b0, 0, 0x7fff3102df20) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x107cf40, 0x10993b0, 0, 0x7fff3102df20) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x10997e0, 2, 0x7fff3102deb8, 0x10dacf0) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x10993b0, 2, 0x7fff3102dfa0, 0x2b33a4907fb4) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x10993b0, 6, 0x10daae0, 100)            = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 8, 0x7fff3102de9c, 0x2b33a4907fb4)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 7, 0x7fff3102deaa, 0x2b33a4907fb4)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 21, 0x7fff3102de94, 0)                  = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 22, 0x7fff3102de96, 0)                  = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 20, 0x7fff3102df20, 0x10daf00)          = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 0x300b, 0x10da5f0, 0x10db1f0)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 0x3009, 0x10da5a0, 0x10db1f0)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 0x300a, 0x10da5a8, 0x10db1f0)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 0x3003, 0x7fff3102ded0, 0x10db1f0 <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x1098d50, 0x3003, 0x7fff3102ded0, 0x10db1f0) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 0x3007, 0x7fff3102ded0, 0x7fff3102dbac <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x1098d50, 0x3007, 0x7fff3102ded0, 0x7fff3102dbac) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 0x3008, 0x7fff3102dea4, 0x7fff3102dbac <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x1098d50, 0x3008, 0x7fff3102dea4, 0x7fff3102dbac) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 0x3002, 0x7fff3102ded0, 0x7fff3102dbac <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x1098d50, 0x3002, 0x7fff3102ded0, 0x7fff3102dbac) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 6, 0x10da82c, 0x7fff3102dbac)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 0xa007, 0x10da590, 0x7fff3102dbac)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 0xa00a, 0x7fff3102dea0, 0x7fff3102dbac) = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 18, 0x7fff3102ded0, 0x7fff3102dbac)     = 0
libamdhip64.so.3->hsa_agent_get_info(0x1098d50, 0xa012, 0x7fff3102dea4, 0x7fff3102dbac) = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x1026c40, 160, 0, 0x7fff3102df08 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(0, 4096, 64, 0x7fff3102de28)                   = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(4, 0x10b6b00, 0, 0x2b33a2fb3000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b33a2fb3000, 0x7fff3102dcc0, 0, 0x2b33a42cc160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b33a2fb3000, 4096, 0x7fff3102ddc8, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x103dd30, 0x101000, 0, 0x7fff3102e088 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(3, 0x101000, 8256, 0x7fff3102dfa8)             = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(4, 0x10b6b00, 0, 0x2b34ad100000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b34ad100000, 0x7fff3102de40, 0, 0x2b33a42cc160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b34ad100000, 0x101000, 0x7fff3102df48, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x103dd30, 0x101000, 0, 0x7fff3102e088 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(3, 0x101000, 8256, 0x7fff3102dfa8)             = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(4, 0x10b6b00, 0, 0x2b34ad300000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b34ad300000, 0x7fff3102de40, 0, 0x2b33a42cc160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b34ad300000, 0x101000, 0x7fff3102df48, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_signal_create(1, 0, 0, 0x10daad0 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtCreateEvent(0x7fff3102e070, 0, 0, 0x7fff3102e060)          = 0
<... hsa_signal_create resumed> )                                                       = 0
[detect_cuda_device] Querying CUDA devices:
[detect_cuda_device]   Device 0 Device 66a1, CUDA cores 128, global memory size 16368 MB, compute capability 9.0.
[detect_cuda_device]   Device 1 Device 66a1, CUDA cores 128, global memory size 16368 MB, compute capability 9.0.
[detect_cuda_device]   Device 2 Device 66a1, CUDA cores 128, global memory size 16368 MB, compute capability 9.0.
[detect_cuda_device]   Device 3 Device 66a1, CUDA cores 128, global memory size 16368 MB, compute capability 9.0.
[detect_cuda_device] Using CUDA device 0, global memory size 16368 MB.
[aln_core] Loading BWTs, please wait..
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x1045840, 0x459900, 0, 0x7fff3102e158 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(4, 0x600000, 8385, 0x7fff3102e078)             = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b34ada00000, 0x600000, 0x7fff3102e078, 0) = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(3, 0x10b74c0, 0, 0x2b34ada00000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b34ada00000, 0x7fff3102df10, 0, 0x2b33a42cc160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b34ada00000, 0x600000, 0x7fff3102e018, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x1045840, 0x459900, 0, 0x7fff3102e158 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(4, 0x600000, 8385, 0x7fff3102e078)             = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b37b6400000, 0x600000, 0x7fff3102e078, 0) = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(3, 0x10b74c0, 0, 0x2b37b6400000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b37b6400000, 0x7fff3102df10, 0, 0x2b33a42cc160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b37b6400000, 0x600000, 0x7fff3102e018, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_executable_create_alt(1, 0, 0, 0x10df0e0)                         = 0
libamdhip64.so.3->hsa_code_object_reader_create_from_memory(0x42064d, 0x13930, 0x10df0e8, 0x2b37b803bd00) = 0
libamdhip64.so.3->hsa_executable_load_agent_code_object(0x10f2b30, 0x10451e0, 0x10f2210, 0 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(0, 0x10000, 64, 0x7fff3102d208)                = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b33ac3b0000, 0x10000, 0x7fff3102d208, 0) = 0
<... hsa_executable_load_agent_code_object resumed> )                                   = 0
libamdhip64.so.3->hsa_executable_freeze(0x10f2b30, 0, 0x1106bd8, 1)                     = 0
libamdhip64.so.3->hsa_executable_get_symbol_by_name(0x10f2b30, 0x1110e88, 0x7fff3102d9b8, 0x7fff3102d9b0) = 0
libamdhip64.so.3->hsa_executable_symbol_get_info(0x1111370, 22, 0x10f24c0, 0x10f20c0)   = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 6, 0x7fff3102d9c8, 0x2b33a4909ea4)      = 0
libamdhip64.so.3->hsa_executable_get_symbol_by_name(0x10f2b30, 0x10df238, 0x7fff3102d9b8, 0x7fff3102d9b0) = 0
libamdhip64.so.3->hsa_executable_symbol_get_info(0x1111570, 22, 0x11121c0, 0x10f20c0)   = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 6, 0x7fff3102d9c8, 0x2b33a4909ea4)      = 0
libamdhip64.so.3->hsa_executable_get_symbol_by_name(0x10f2b30, 0x10f2538, 0x7fff3102d9b8, 0x7fff3102d9b0) = 0
libamdhip64.so.3->hsa_executable_symbol_get_info(0x1111780, 22, 0x1112af0, 0x1112f90)   = 0
libamdhip64.so.3->hsa_agent_get_info(0x10451e0, 6, 0x7fff3102d9c8, 0x2b33a4909ea4)      = 0
libamdhip64.so.3->hsa_executable_get_symbol_by_name(0x10f2b30, 0xf9ea48, 0x7fff3102e2d8, 0x7fff3102e2e0) = 0
libamdhip64.so.3->hsa_executable_symbol_get_info(0x1111cc0, 0, 0x7fff3102e2d4, 0x1106a00) = 0
libamdhip64.so.3->hsa_executable_symbol_get_info(0x1111cc0, 9, 0x1111fc0, 0x7fff3102e2d4) = 0
libamdhip64.so.3->hsa_executable_symbol_get_info(0x1111cc0, 21, 0x1111fb8, 0x2b33a4909f00) = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x1045840, 0x459900, 0, 0x7fff3102e158 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(4, 0x600000, 8385, 0x7fff3102e078)             = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b37b6c00000, 0x600000, 0x7fff3102e078, 0) = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(3, 0x10b74c0, 0, 0x2b37b6c00000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b37b6c00000, 0x7fff3102df10, 0, 0x2b33a42cc160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b37b6c00000, 0x600000, 0x7fff3102e018, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x1045840, 0x459900, 0, 0x7fff3102e158 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(4, 0x600000, 8385, 0x7fff3102e078)             = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b37b7400000, 0x600000, 0x7fff3102e078, 0) = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(3, 0x10b74c0, 0, 0x2b37b7400000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b37b7400000, 0x7fff3102df10, 0, 0x2b33a42cc160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b37b7400000, 0x600000, 0x7fff3102e018, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_executable_get_symbol_by_name(0x10f2b30, 0xf9eb08, 0x7fff3102e2d8, 0x7fff3102e2e0) = 0
libamdhip64.so.3->hsa_executable_symbol_get_info(0x1111ea0, 0, 0x7fff3102e2d4, 0x10f2000) = 0
libamdhip64.so.3->hsa_executable_symbol_get_info(0x1111ea0, 9, 0x1106ab0, 0x7fff3102e2d4) = 0
libamdhip64.so.3->hsa_executable_symbol_get_info(0x1111ea0, 21, 0x1106aa8, 0x2b33a4909f00) = 0
[aln_core] Finished loading reference sequence assembly, 8 MB in 3.33s (2.40 MB/s).
[aln_core] Sweet! Running with an enlarged buffer for the Tesla/Quadro series.
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x1045840, 0x800000, 0, 0x7fff3102dc78 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(4, 0x800000, 8385, 0x7fff3102db98)             = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b37bc200000, 0x800000, 0x7fff3102db98, 0) = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(3, 0x10b74c0, 0, 0x2b37bc200000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b37bc200000, 0x7fff3102da30, 0, 0x2b33a42cc160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b37bc200000, 0x800000, 0x7fff3102db38, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x1045840, 0x800000, 0, 0x7fff3102dc78 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(4, 0x800000, 8385, 0x7fff3102db98)             = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b37bd400000, 0x800000, 0x7fff3102db98, 0) = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(3, 0x10b74c0, 0, 0x2b37bd400000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b37bd400000, 0x7fff3102da30, 0, 0x2b33a42cc160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b37bd400000, 0x800000, 0x7fff3102db38, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x1045840, 88, 0, 0x7fff3102dc78)        = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(3, 0x10b74c0, 0, 0x2b34afa18000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b34afa18000, 0x7fff3102da30, 0, 0x2b33a42cc160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b34afa00000, 0x200000, 0x7fff3102db38, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_executable_get_symbol_by_name(0x10f2b30, 0xf9ebd8, 0x7fff3102ddf8, 0x7fff3102de00) = 0
libamdhip64.so.3->hsa_executable_symbol_get_info(0x1111db0, 0, 0x7fff3102ddf4, 0x10f2000) = 0
libamdhip64.so.3->hsa_executable_symbol_get_info(0x1111db0, 9, 0x1114a30, 0x7fff3102ddf4) = 0
libamdhip64.so.3->hsa_executable_symbol_get_info(0x1111db0, 21, 0x1114a28, 0x2b33a4909f00) = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x1045840, 0x2b000000, 0, 0x7fff3102dc78 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(4, 0x2b000000, 8385, 0x7fff3102db98)           = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b37be600000, 0x2b000000, 0x7fff3102db98, 0) = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(3, 0x10b74c0, 0, 0x2b37be600000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b37be600000, 0x7fff3102da30, 0, 0x2b33a42cc160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b37be600000, 0x2b000000, 0x7fff3102db38, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x1045840, 0x80000, 0, 0x7fff3102dbf8)   = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(3, 0x10b74c0, 0, 0x2b34afa19000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b34afa19000, 0x7fff3102d9b0, 0, 0x2b33a42cc160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b34afa00000, 0x200000, 0x7fff3102dab8, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x1045840, 0x800000, 0, 0x7fff3102dbf8 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(4, 0x800000, 8385, 0x7fff3102db18)             = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b3840200000, 0x800000, 0x7fff3102db18, 0) = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(3, 0x10b74c0, 0, 0x2b3840200000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b3840200000, 0x7fff3102d9b0, 0, 0x2b33a42cc160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b3840200000, 0x800000, 0x7fff3102dab8, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                                   =0
[aln_core] Now aligning sequence reads to reference assembly, please wait..
[aln_core] Processing 67584 sequence reads at a time.
[aln_core] cuda_inexact_match_caller..Memory access fault by GPU node-4 (Agent handle: 0x10451e0) on address (nil). Reason: Page not present or supervisor privilege.
</details>

<details>
  <summary>correct</summary>
Barracuda, Version 0.6.2 beta
[aln_core] 20bp reads: max_diff = 2
[aln_core] 38bp reads: max_diff = 3
[aln_core] 64bp reads: max_diff = 4
[aln_core] 93bp reads: max_diff = 5
[aln_core] 124bp reads: max_diff = 6
[aln_core] Running CUDA mode.
libamdhip64.so.3->hsa_init(0, 0x7ffcfdb582d8, 0x2b322d938d90, 0x1541150 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtOpenKFD(0x2b322e121338, 0x2b322e4e8778, 0xffffffff, 0x153db00) = 0
libhsa-runtime64.so.1->hsaKmtGetVersion(0x7ffcfdb57f58, 0, 0, 48)                       = 0
libhsa-runtime64.so.1->hsaKmtReleaseSystemProperties(2, 0x80084b01, 0, -1)              = 0
libhsa-runtime64.so.1->hsaKmtAcquireSystemProperties(0x7ffcfdb57f60, 0, 0x2b3235b9dea0, 0x153de00) = 0
libhsa-runtime64.so.1->hsaKmtGetNodeProperties(0, 0x7ffcfdb57ff0, 0, 0)                 = 0
libhsa-runtime64.so.1->hsaKmtGetNodeMemoryProperties(0, 1, 0x153cd80, 4)                = 0
libhsa-runtime64.so.1->hsaKmtGetNodeCacheProperties(0, 0, 26, 0x15c32c0)                = 0
libhsa-runtime64.so.1->hsaKmtGetNodeIoLinkProperties(0, 7, 0x15ca1e0, 0x15ca1e0)        = 0
libhsa-runtime64.so.1->hsaKmtGetNodeProperties(1, 0x7ffcfdb57ff0, 0x2b322e4e8fe0, 0)    = 0
libhsa-runtime64.so.1->hsaKmtGetNodeMemoryProperties(1, 1, 0x1544180, 0)                = 0
libhsa-runtime64.so.1->hsaKmtGetNodeCacheProperties(1, 16, 26, 0x15cab80)               = 0
libhsa-runtime64.so.1->hsaKmtGetNodeIoLinkProperties(1, 7, 0x15d1c90, 0x15d1c90)        = 0
libhsa-runtime64.so.1->hsaKmtGetNodeProperties(2, 0x7ffcfdb57ff0, 49, 0)                = 0
libhsa-runtime64.so.1->hsaKmtGetNodeMemoryProperties(2, 1, 0x1544180, 0)                = 0
libhsa-runtime64.so.1->hsaKmtGetNodeCacheProperties(2, 32, 26, 0x15d2610)               = 0
libhsa-runtime64.so.1->hsaKmtGetNodeIoLinkProperties(2, 7, 0x15d9760, 0x15d9760)        = 0
libhsa-runtime64.so.1->hsaKmtGetNodeProperties(3, 0x7ffcfdb57ff0, 33, 0)                = 0
libhsa-runtime64.so.1->hsaKmtGetNodeMemoryProperties(3, 1, 0x15d9940, 0x15d9940)        = 0
libhsa-runtime64.so.1->hsaKmtGetNodeCacheProperties(3, 48, 26, 0x15da0f0)               = 0
libhsa-runtime64.so.1->hsaKmtGetNodeIoLinkProperties(3, 7, 0x15e11e0, 0x15e11e0)        = 0
libhsa-runtime64.so.1->hsaKmtGetNodeProperties(4, 0x7ffcfdb57ff0, 0x9cd0, 0)            = 0
libhsa-runtime64.so.1->hsaKmtGetNodeIoLinkProperties(4, 7, 0x15e11e0, 0x15e11e0)        = 0
libhsa-runtime64.so.1->hsaKmtGetNodeProperties(5, 0x7ffcfdb57ff0, 0x9cd0, 0)            = 0
libhsa-runtime64.so.1->hsaKmtGetNodeIoLinkProperties(5, 7, 0x15e1200, 0x15e1200)        = 0
libhsa-runtime64.so.1->hsaKmtGetNodeProperties(6, 0x7ffcfdb57ff0, 0x9cb0, 0)            = 0
libhsa-runtime64.so.1->hsaKmtGetNodeIoLinkProperties(6, 7, 0x15e1200, 0x15e1200)        = 0
libhsa-runtime64.so.1->hsaKmtGetNodeProperties(7, 0x7ffcfdb57ff0, 0x9cb0, 0)            = 0
libhsa-runtime64.so.1->hsaKmtGetNodeIoLinkProperties(7, 7, 0x15e1200, 0x15e1200)        = 0
libhsa-runtime64.so.1->hsaKmtGetNodeProperties(4, 0x7ffcfdb57ff0, 0x15ca1a0, 0)         = 0
libhsa-runtime64.so.1->hsaKmtGetClockCounters(4, 0x15e14e0, 0, 0)                       = 0
libhsa-runtime64.so.1->hsaKmtGetNodeMemoryProperties(4, 5, 0x15e1790, 12)               = 0
libhsa-runtime64.so.1->hsaKmtGetNodeCacheProperties(4, 0x80001000, 96, 0x15e2400)       = 0
libhsa-runtime64.so.1->hsaKmtGetNodeProperties(5, 0x7ffcfdb57ff0, 0x15ca1a0, 0)         = 0
libhsa-runtime64.so.1->hsaKmtGetClockCounters(5, 0x15fd390, 0, 0)                       = 0
libhsa-runtime64.so.1->hsaKmtGetNodeMemoryProperties(5, 5, 0x15fd610, 12)               = 0
libhsa-runtime64.so.1->hsaKmtGetNodeCacheProperties(5, 0x80001040, 96, 0x15fe280)       = 0
libhsa-runtime64.so.1->hsaKmtGetNodeProperties(6, 0x7ffcfdb57ff0, 0x15ca1a0, 0x15e1800) = 0
libhsa-runtime64.so.1->hsaKmtGetClockCounters(6, 0x1619240, 0, 0)                       = 0
libhsa-runtime64.so.1->hsaKmtGetNodeMemoryProperties(6, 5, 0x1619490, 12)               = 0
libhsa-runtime64.so.1->hsaKmtGetNodeCacheProperties(6, 0x80001080, 96, 0x161a0c0)       = 0
libhsa-runtime64.so.1->hsaKmtGetNodeProperties(7, 0x7ffcfdb57ff0, 0x15ca1a0, 0x15e1c00) = 0
libhsa-runtime64.so.1->hsaKmtGetClockCounters(7, 0x1635050, 0, 0)                       = 0
libhsa-runtime64.so.1->hsaKmtGetNodeMemoryProperties(7, 5, 0x1635300, 12)               = 0
libhsa-runtime64.so.1->hsaKmtGetNodeCacheProperties(7, 0x800010c0, 96, 0x1635f30)       = 0
libhsa-runtime64.so.1->hsaKmtGetClockCounters(0, 0x7ffcfdb581b0, 1, 0x15ca100)          = 0
libhsa-runtime64.so.1->hsaKmtCreateEvent(0x7ffcfdb58160, 1, 0, 0x7ffcfdb58158 <unfinished ...>
libhsakmt.so.1->hsaKmtAllocMemory(0, 0x8000, 4161, 0x7ffcfdb580a0)                      = 0
libhsakmt.so.1->hsaKmtMapMemoryToGPU(0x2b322ce60000, 0x8000, 0x7ffcfdb580a8, -1)        = 0
<... hsaKmtCreateEvent resumed> )                                                       = 0
libhsa-runtime64.so.1->hsaKmtAllocMemory(0, 4096, 64, 0x7ffcfdb58008)                   = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b322ce5e000, 4096, 0x7ffcfdb58008, 0) = 0
libhsa-runtime64.so.1->hsaKmtCreateEvent(0x7ffcfdb58060, 0, 0, 0x7ffcfdb58050)          = 0
libhsa-runtime64.so.1->hsaKmtAllocMemory(4, 0x100000000, 576, 0x7ffcfdb58130)           = 0
libhsa-runtime64.so.1->hsaKmtAllocMemory(0, 8192, 64, 0x7ffcfdb580f8)                   = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b322ce6a000, 8192, 0x7ffcfdb580f8, 0) = 0
libhsa-runtime64.so.1->hsaKmtAllocMemory(0, 4096, 4160, 0x7ffcfdb57e88)                 = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b322ce6d000, 4096, 0x7ffcfdb57e88, 0) = 0
libhsa-runtime64.so.1->hsaKmtSetTrapHandler(4, 0x2b322ce6d000, 4096, 0x2b322ce6a000)    = 0
libhsa-runtime64.so.1->hsaKmtAllocMemory(5, 0x100000000, 576, 0x7ffcfdb58130)           = 0
libhsa-runtime64.so.1->hsaKmtAllocMemory(0, 8192, 64, 0x7ffcfdb580f8)                   = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b322ce70000, 8192, 0x7ffcfdb580f8, 0) = 0
libhsa-runtime64.so.1->hsaKmtAllocMemory(0, 4096, 4160, 0x7ffcfdb57e88)                 = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b322ce73000, 4096, 0x7ffcfdb57e88, 0) = 0
libhsa-runtime64.so.1->hsaKmtSetTrapHandler(5, 0x2b322ce73000, 4096, 0x2b322ce70000)    = 0
libhsa-runtime64.so.1->hsaKmtAllocMemory(6, 0x100000000, 576, 0x7ffcfdb58130)           = 0
libhsa-runtime64.so.1->hsaKmtAllocMemory(0, 8192, 64, 0x7ffcfdb580f8)                   = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b322ce76000, 8192, 0x7ffcfdb580f8, 0) = 0
libhsa-runtime64.so.1->hsaKmtAllocMemory(0, 4096, 4160, 0x7ffcfdb57e88)                 = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b322ce79000, 4096, 0x7ffcfdb57e88, 0) = 0
libhsa-runtime64.so.1->hsaKmtSetTrapHandler(6, 0x2b322ce79000, 4096, 0x2b322ce76000)    = 0
libhsa-runtime64.so.1->hsaKmtAllocMemory(7, 0x100000000, 576, 0x7ffcfdb58130)           = 0
libhsa-runtime64.so.1->hsaKmtAllocMemory(0, 8192, 64, 0x7ffcfdb580f8)                   = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b322ce7c000, 8192, 0x7ffcfdb580f8, 0) = 0
libhsa-runtime64.so.1->hsaKmtAllocMemory(0, 4096, 4160, 0x7ffcfdb57e88)                 = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b322ce7f000, 4096, 0x7ffcfdb57e88, 0) = 0
libhsa-runtime64.so.1->hsaKmtSetTrapHandler(7, 0x2b322ce7f000, 4096, 0x2b322ce7c000)    = 0
<... hsa_init resumed> )                                                                = 0
libamdhip64.so.3->hsa_system_get_major_extension_table(513, 1, 24, 0x2b322dc01fa0)      = 0
libamdhip64.so.3->hsa_iterate_agents(0x2b322d928e20, 0, 0x7ffcfdb58178, 0x2b322dc01fa8 <unfinished ...>
libamdhip64.so.3->hsa_agent_get_info(0x15c2a60, 17, 0x7ffcfdb5815c, 0x2b322dc01fa8)     = 0
libamdhip64.so.3->hsa_amd_agent_iterate_memory_pools(0x15c2a60, 0x2b322d925a80, 0x7ffcfdb58160, 0x2b322dc01fa8 <unfinished ...>
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15c2c40, 0, 0x7ffcfdb580b8, 0x7ffcfdb58160) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15c2c40, 1, 0x7ffcfdb580bc, 0x2b322e7e2fb4) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15c2f80, 0, 0x7ffcfdb580b8, 0x2b322e7e2fb4) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15c2f80, 1, 0x7ffcfdb580bc, 0x2b322e7e2fb4) = 0
<... hsa_amd_agent_iterate_memory_pools resumed> )                                      = 1
libamdhip64.so.3->hsa_agent_get_info(0x15ca1e0, 17, 0x7ffcfdb5815c, 0)                  = 0
libamdhip64.so.3->hsa_amd_agent_iterate_memory_pools(0x15ca1e0, 0x2b322d925a80, 0x7ffcfdb58160, 0 <unfinished ...>
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15ca3c0, 0, 0x7ffcfdb580b8, 0x7ffcfdb58160) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15ca3c0, 1, 0x7ffcfdb580bc, 0x2b322e7e2fb4) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15ca7a0, 0, 0x7ffcfdb580b8, 0x2b322e7e2fb4) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15ca7a0, 1, 0x7ffcfdb580bc, 0x2b322e7e2fb4) = 0
<... hsa_amd_agent_iterate_memory_pools resumed> )                                      = 1
libamdhip64.so.3->hsa_agent_get_info(0x15d1c90, 17, 0x7ffcfdb5815c, 0x1651000)          = 0
libamdhip64.so.3->hsa_amd_agent_iterate_memory_pools(0x15d1c90, 0x2b322d925a80, 0x7ffcfdb58160, 0x1651000 <unfinished ...>
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15d1e70, 0, 0x7ffcfdb580b8, 0x7ffcfdb58160) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15d1e70, 1, 0x7ffcfdb580bc, 0x2b322e7e2fb4) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15d2230, 0, 0x7ffcfdb580b8, 0x2b322e7e2fb4) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15d2230, 1, 0x7ffcfdb580bc, 0x2b322e7e2fb4) = 0
<... hsa_amd_agent_iterate_memory_pools resumed> )                                      = 1
libamdhip64.so.3->hsa_agent_get_info(0x15d9760, 17, 0x7ffcfdb5815c, 0x1652500)          = 0
libamdhip64.so.3->hsa_amd_agent_iterate_memory_pools(0x15d9760, 0x2b322d925a80, 0x7ffcfdb58160, 0x1652500 <unfinished ...>
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15d9970, 0, 0x7ffcfdb580b8, 0x7ffcfdb58160) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15d9970, 1, 0x7ffcfdb580bc, 0x2b322e7e2fb4) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15d9d30, 0, 0x7ffcfdb580b8, 0x2b322e7e2fb4) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15d9d30, 1, 0x7ffcfdb580bc, 0x2b322e7e2fb4) = 0
<... hsa_amd_agent_iterate_memory_pools resumed> )                                      = 1
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 17, 0x7ffcfdb5815c, 0x2b322e7e2fb4)     = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 17, 0x7ffcfdb5815c, 0)                  = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 17, 0x7ffcfdb5815c, 0x1651000)          = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 17, 0x7ffcfdb5815c, 0x1652900)          = 0
<... hsa_iterate_agents resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 0xa000, 0x7ffcfdb58288, 0x1652a38)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 0, 0x7ffcfdb58290, 0x1652a38)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 4, 0x1653280, 0x2b322dbb2920)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 0xa010, 0x7ffcfdb58120, 0x2b322dbb2920) = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 0xa006, 0x7ffcfdb58124, 0x1652020)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 19, 0x7ffcfdb57e70, 0x1652020)          = 0
libamdhip64.so.3->hsa_isa_get_info_alt(0x14ab770, 0, 0x7ffcfdb57e58, 0x1652020)         = 0
libamdhip64.so.3->hsa_isa_get_info_alt(0x14ab770, 1, 0x1653171, 0x1652500)              = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 0xa009, 0x7ffcfdb57ea0, 0)              = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 0xa002, 0x1652cf4, 0)                   = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 0xa001, 0x1652dfc, 0x1652a70)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 18, 0x7ffcfdb57e80, 0x1652a70)          = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 0xa003, 0x1652d68, 0x16534b0)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 0xa008, 0x1652d6c, 0x16534b0)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 0xa007, 0x1653014, 0x16534b0)           = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x15e11e0, 0x15c2c40, 1, 0x7ffcfdb57dd8) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x15e11e0, 0x15c2c40, 2, 0x1652550) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x15e11e0, 0x15ca3c0, 1, 0x7ffcfdb57dd8) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x15e11e0, 0x15ca3c0, 2, 0x16534c0) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x15e11e0, 0x15d1e70, 1, 0x7ffcfdb57dd8) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x15e11e0, 0x15d1e70, 2, 0x16534c0) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x15e11e0, 0x15d9970, 1, 0x7ffcfdb57dd8) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x15e11e0, 0x15d9970, 2, 0x16534c0) = 0
libamdhip64.so.3->hsa_amd_agent_iterate_memory_pools(0x15e11e0, 0x2b322d925b10, 0x1652ca0, 0x2b322dbfd440 <unfinished ...>
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15e1840, 0, 0x7ffcfdb57db4, 0x1652ca0) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15e1840, 1, 0x7ffcfdb57db8, 0x2b322e7e2fb4) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x15c2a60, 0x15e1840, 0, 0x7ffcfdb57dbc) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15e1c90, 0, 0x7ffcfdb57db4, 4)         = 0
<... hsa_amd_agent_iterate_memory_pools resumed> )                                      = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x15fd090, 0x15e1840, 0, 0x7ffcfdb57ee0) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1618f40, 0x15e1840, 0, 0x7ffcfdb57ee0) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1634d50, 0x15e1840, 0, 0x7ffcfdb57ee0) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15e1c90, 2, 0x7ffcfdb57e78, 0x16534c0) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15e1840, 2, 0x7ffcfdb57f60, 0x2b322e7e2fb4) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15e1840, 6, 0x16532c0, 100)            = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 8, 0x7ffcfdb57e5c, 0x2b322e7e2fb4)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 7, 0x7ffcfdb57e6a, 0x2b322e7e2fb4)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 21, 0x7ffcfdb57e54, 0)                  = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 22, 0x7ffcfdb57e56, 0)                  = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 20, 0x7ffcfdb57ee0, 0x1652500)          = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 0x300b, 0x1652dd0, 0)                   = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 0x3009, 0x1652d80, 0)                   = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 0x300a, 0x1652d88, 0)                   = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 0x3003, 0x7ffcfdb57e90, 0 <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x15e11e0, 0x3003, 0x7ffcfdb57e90, 0 <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_agent_iterate_memory_pools(0x15c2a60, 0x2b322e7cf730, 0x1653610, 8) = 1
libhsa-runtime64.so.1->hsaKmtGetTileConfig(4, 0x7ffcfdb57860, 0x7ffcfdb57830, 6)        = 0
libhsa-runtime64.so.1->hsaKmtGetTileConfig(5, 0x7ffcfdb57860, 0x7ffcfdb57830, 6)        = 0
libhsa-runtime64.so.1->hsaKmtGetTileConfig(6, 0x7ffcfdb57860, 0x7ffcfdb57830, 6)        = 0
libhsa-runtime64.so.1->hsaKmtGetTileConfig(7, 0x7ffcfdb57860, 0x7ffcfdb57830, 6)        = 0
<... hsa_amd_image_get_info_max_dim resumed> )                                          = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 0x3007, 0x7ffcfdb57e90, 0x7ffcfdb57b6c <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x15e11e0, 0x3007, 0x7ffcfdb57e90, 0x7ffcfdb57b6c) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 0x3008, 0x7ffcfdb57e64, 0x7ffcfdb57b6c <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x15e11e0, 0x3008, 0x7ffcfdb57e64, 0x7ffcfdb57b6c) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 0x3002, 0x7ffcfdb57e90, 0x7ffcfdb57b6c <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x15e11e0, 0x3002, 0x7ffcfdb57e90, 0x7ffcfdb57b6c) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 6, 0x165300c, 0x7ffcfdb57b6c)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 0xa007, 0x1652d70, 0x7ffcfdb57b6c)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 0xa00a, 0x7ffcfdb57e60, 0x7ffcfdb57b6c) = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 18, 0x7ffcfdb57e90, 0x7ffcfdb57b6c)     = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 0xa012, 0x7ffcfdb57e64, 0x7ffcfdb57b6c) = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x15c2f80, 0x101000, 0, 0x7ffcfdb58048 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(0, 0x101000, 8256, 0x7ffcfdb57f68)             = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(4, 0x1652b00, 0, 0x2b3236200000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b3236200000, 0x7ffcfdb57e00, 0, 0x2b322e1a7160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b3236200000, 0x101000, 0x7ffcfdb57f08, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x15c2f80, 0x101000, 0, 0x7ffcfdb58048 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(0, 0x101000, 8256, 0x7ffcfdb57f68)             = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(4, 0x1652b00, 0, 0x2b3236400000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b3236400000, 0x7ffcfdb57e00, 0, 0x2b322e1a7160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b3236400000, 0x101000, 0x7ffcfdb57f08, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_signal_create(1, 0, 0, 0x16532b0 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtCreateEvent(0x7ffcfdb58030, 0, 0, 0x7ffcfdb58020)          = 0
<... hsa_signal_create resumed> )                                                       = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 0xa000, 0x7ffcfdb58288, 0x1674448)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 0, 0x7ffcfdb58290, 0x1674448)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 4, 0x16742c0, 0x2b322dbb2920)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 0xa010, 0x7ffcfdb58120, 0x2b322dbb2920) = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 0xa006, 0x7ffcfdb58124, 0x16744f0)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 19, 0x7ffcfdb57e70, 0x16744f0)          = 0
libamdhip64.so.3->hsa_isa_get_info_alt(0x14ab770, 0, 0x7ffcfdb57e58, 0x16744f0)         = 0
libamdhip64.so.3->hsa_isa_get_info_alt(0x14ab770, 1, 0x16741b1, 0x1674700)              = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 0xa009, 0x7ffcfdb57ea0, 0)              = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 0xa002, 0x1673d34, 0)                   = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 0xa001, 0x1673e3c, 0x16738c0)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 18, 0x7ffcfdb57e80, 0x16738c0)          = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 0xa003, 0x1673da8, 0x1674520)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 0xa008, 0x1673dac, 0x1674520)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 0xa007, 0x1674054, 0x1674520)           = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x15fd090, 0x15c2c40, 1, 0x7ffcfdb57dd8) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x15fd090, 0x15c2c40, 2, 0x1673870) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x15fd090, 0x15ca3c0, 1, 0x7ffcfdb57dd8) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x15fd090, 0x15ca3c0, 2, 0x1673870) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x15fd090, 0x15d1e70, 1, 0x7ffcfdb57dd8) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x15fd090, 0x15d1e70, 2, 0x1673870) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x15fd090, 0x15d9970, 1, 0x7ffcfdb57dd8) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x15fd090, 0x15d9970, 2, 0x1673870) = 0
libamdhip64.so.3->hsa_amd_agent_iterate_memory_pools(0x15fd090, 0x2b322d925b10, 0x1673ce0, 0x2b322dbfd440 <unfinished ...>
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15fd6c0, 0, 0x7ffcfdb57db4, 0x1673ce0) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15fd6c0, 1, 0x7ffcfdb57db8, 0x2b322e7e2fb4) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x15ca1e0, 0x15fd6c0, 0, 0x7ffcfdb57dbc) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15fdb10, 0, 0x7ffcfdb57db4, 5)         = 0
<... hsa_amd_agent_iterate_memory_pools resumed> )                                      = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x15e11e0, 0x15fd6c0, 0, 0x7ffcfdb57ee0) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1618f40, 0x15fd6c0, 0, 0x7ffcfdb57ee0) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1634d50, 0x15fd6c0, 0, 0x7ffcfdb57ee0) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15fdb10, 2, 0x7ffcfdb57e78, 0x1673870) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15fd6c0, 2, 0x7ffcfdb57f60, 0x2b322e7e2fb4) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x15fd6c0, 6, 0x1674300, 100)            = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 8, 0x7ffcfdb57e5c, 0x2b322e7e2fb4)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 7, 0x7ffcfdb57e6a, 0x2b322e7e2fb4)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 21, 0x7ffcfdb57e54, 0)                  = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 22, 0x7ffcfdb57e56, 0)                  = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 20, 0x7ffcfdb57ee0, 0x1674500)          = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 0x300b, 0x1673e10, 0)                   = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 0x3009, 0x1673dc0, 0)                   = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 0x300a, 0x1673dc8, 0)                   = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 0x3003, 0x7ffcfdb57e90, 0 <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x15fd090, 0x3003, 0x7ffcfdb57e90, 0) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 0x3007, 0x7ffcfdb57e90, 0x7ffcfdb57b6c <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x15fd090, 0x3007, 0x7ffcfdb57e90, 0x7ffcfdb57b6c) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 0x3008, 0x7ffcfdb57e64, 0x7ffcfdb57b6c <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x15fd090, 0x3008, 0x7ffcfdb57e64, 0x7ffcfdb57b6c) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 0x3002, 0x7ffcfdb57e90, 0x7ffcfdb57b6c <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x15fd090, 0x3002, 0x7ffcfdb57e90, 0x7ffcfdb57b6c) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 6, 0x167404c, 0x7ffcfdb57b6c)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 0xa007, 0x1673db0, 0x7ffcfdb57b6c)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 0xa00a, 0x7ffcfdb57e60, 0x7ffcfdb57b6c) = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 18, 0x7ffcfdb57e90, 0x7ffcfdb57b6c)     = 0
libamdhip64.so.3->hsa_agent_get_info(0x15fd090, 0xa012, 0x7ffcfdb57e64, 0x7ffcfdb57b6c) = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x15ca7a0, 0x101000, 0, 0x7ffcfdb58048 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(1, 0x101000, 8256, 0x7ffcfdb57f68)             = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(4, 0x1652b00, 0, 0x2b3236600000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b3236600000, 0x7ffcfdb57e00, 0, 0x2b322e1a7160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b3236600000, 0x101000, 0x7ffcfdb57f08, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x15ca7a0, 0x101000, 0, 0x7ffcfdb58048 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(1, 0x101000, 8256, 0x7ffcfdb57f68)             = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(4, 0x1652b00, 0, 0x2b3236800000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b3236800000, 0x7ffcfdb57e00, 0, 0x2b322e1a7160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b3236800000, 0x101000, 0x7ffcfdb57f08, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_signal_create(1, 0, 0, 0x16742f0 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtCreateEvent(0x7ffcfdb58030, 0, 0, 0x7ffcfdb58020)          = 0
<... hsa_signal_create resumed> )                                                       = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 0xa000, 0x7ffcfdb58288, 0x1674cf8)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 0, 0x7ffcfdb58290, 0x1674cf8)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 4, 0x16756e0, 0x2b322dbb2920)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 0xa010, 0x7ffcfdb58120, 0x2b322dbb2920) = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 0xa006, 0x7ffcfdb58124, 0)              = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 19, 0x7ffcfdb57e70, 0)                  = 0
libamdhip64.so.3->hsa_isa_get_info_alt(0x14ab770, 0, 0x7ffcfdb57e58, 0)                 = 0
libamdhip64.so.3->hsa_isa_get_info_alt(0x14ab770, 1, 0x16755d1, 0x1675b00)              = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 0xa009, 0x7ffcfdb57ea0, 0)              = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 0xa002, 0x1675154, 0)                   = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 0xa001, 0x167525c, 0x1675800)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 18, 0x7ffcfdb57e80, 0x1675800)          = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 0xa003, 0x16751c8, 0x1675910)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 0xa008, 0x16751cc, 0x1675910)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 0xa007, 0x1675474, 0x1675910)           = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1618f40, 0x15c2c40, 1, 0x7ffcfdb57dd8) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1618f40, 0x15c2c40, 2, 0x16758f0) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1618f40, 0x15ca3c0, 1, 0x7ffcfdb57dd8) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1618f40, 0x15ca3c0, 2, 0x16758f0) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1618f40, 0x15d1e70, 1, 0x7ffcfdb57dd8) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1618f40, 0x15d1e70, 2, 0x16758f0) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1618f40, 0x15d9970, 1, 0x7ffcfdb57dd8) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1618f40, 0x15d9970, 2, 0x16758f0) = 0
libamdhip64.so.3->hsa_amd_agent_iterate_memory_pools(0x1618f40, 0x2b322d925b10, 0x1675100, 0x2b322dbfd440 <unfinished ...>
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x1619540, 0, 0x7ffcfdb57db4, 0x1675100) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x1619540, 1, 0x7ffcfdb57db8, 0x2b322e7e2fb4) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x15d1c90, 0x1619540, 0, 0x7ffcfdb57dbc) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x1619970, 0, 0x7ffcfdb57db4, 6)         = 0
<... hsa_amd_agent_iterate_memory_pools resumed> )                                      = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x15e11e0, 0x1619540, 0, 0x7ffcfdb57ee0) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x15fd090, 0x1619540, 0, 0x7ffcfdb57ee0) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1634d50, 0x1619540, 0, 0x7ffcfdb57ee0) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x1619970, 2, 0x7ffcfdb57e78, 0x16758f0) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x1619540, 2, 0x7ffcfdb57f60, 0x2b322e7e2fb4) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x1619540, 6, 0x1675720, 100)            = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 8, 0x7ffcfdb57e5c, 0x2b322e7e2fb4)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 7, 0x7ffcfdb57e6a, 0x2b322e7e2fb4)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 21, 0x7ffcfdb57e54, 0)                  = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 22, 0x7ffcfdb57e56, 0)                  = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 20, 0x7ffcfdb57ee0, 0x1675900)          = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 0x300b, 0x1675230, 0x1675f50)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 0x3009, 0x16751e0, 0x1675f50)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 0x300a, 0x16751e8, 0x1675f50)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 0x3003, 0x7ffcfdb57e90, 0x1675f50 <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x1618f40, 0x3003, 0x7ffcfdb57e90, 0x1675f50) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 0x3007, 0x7ffcfdb57e90, 0x7ffcfdb57b6c <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x1618f40, 0x3007, 0x7ffcfdb57e90, 0x7ffcfdb57b6c) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 0x3008, 0x7ffcfdb57e64, 0x7ffcfdb57b6c <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x1618f40, 0x3008, 0x7ffcfdb57e64, 0x7ffcfdb57b6c) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 0x3002, 0x7ffcfdb57e90, 0x7ffcfdb57b6c <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x1618f40, 0x3002, 0x7ffcfdb57e90, 0x7ffcfdb57b6c) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 6, 0x167546c, 0x7ffcfdb57b6c)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 0xa007, 0x16751d0, 0x7ffcfdb57b6c)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 0xa00a, 0x7ffcfdb57e60, 0x7ffcfdb57b6c) = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 18, 0x7ffcfdb57e90, 0x7ffcfdb57b6c)     = 0
libamdhip64.so.3->hsa_agent_get_info(0x1618f40, 0xa012, 0x7ffcfdb57e64, 0x7ffcfdb57b6c) = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x15d2230, 0x101000, 0, 0x7ffcfdb58048 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(2, 0x101000, 8256, 0x7ffcfdb57f68)             = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(4, 0x1652b00, 0, 0x2b3236a00000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b3236a00000, 0x7ffcfdb57e00, 0, 0x2b322e1a7160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b3236a00000, 0x101000, 0x7ffcfdb57f08, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x15d2230, 0x101000, 0, 0x7ffcfdb58048 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(2, 0x101000, 8256, 0x7ffcfdb57f68)             = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(4, 0x1652b00, 0, 0x2b3236c00000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b3236c00000, 0x7ffcfdb57e00, 0, 0x2b322e1a7160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b3236c00000, 0x101000, 0x7ffcfdb57f08, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_signal_create(1, 0, 0, 0x1675710 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtCreateEvent(0x7ffcfdb58030, 0, 0, 0x7ffcfdb58020)          = 0
<... hsa_signal_create resumed> )                                                       = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 0xa000, 0x7ffcfdb58288, 0x16760e8)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 0, 0x7ffcfdb58290, 0x16760e8)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 4, 0x1676aa0, 0x2b322dbb2920)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 0xa010, 0x7ffcfdb58120, 0x2b322dbb2920) = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 0xa006, 0x7ffcfdb58124, 0x1676cb0)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 19, 0x7ffcfdb57e70, 0x1676cb0)          = 0
libamdhip64.so.3->hsa_isa_get_info_alt(0x14ab770, 0, 0x7ffcfdb57e58, 0x1676cb0)         = 0
libamdhip64.so.3->hsa_isa_get_info_alt(0x14ab770, 1, 0x1676991, 0x1676d00)              = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 0xa009, 0x7ffcfdb57ea0, 0)              = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 0xa002, 0x1676514, 0)                   = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 0xa001, 0x167661c, 0x1676bc0)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 18, 0x7ffcfdb57e80, 0x1676bc0)          = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 0xa003, 0x1676588, 0x1676d80)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 0xa008, 0x167658c, 0x1676d80)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 0xa007, 0x1676834, 0x1676d80)           = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1634d50, 0x15c2c40, 1, 0x7ffcfdb57dd8) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1634d50, 0x15c2c40, 2, 0x1676cf0) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1634d50, 0x15ca3c0, 1, 0x7ffcfdb57dd8) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1634d50, 0x15ca3c0, 2, 0x1676cf0) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1634d50, 0x15d1e70, 1, 0x7ffcfdb57dd8) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1634d50, 0x15d1e70, 2, 0x1676cf0) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1634d50, 0x15d9970, 1, 0x7ffcfdb57dd8) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1634d50, 0x15d9970, 2, 0x1676cf0) = 0
libamdhip64.so.3->hsa_amd_agent_iterate_memory_pools(0x1634d50, 0x2b322d925b10, 0x16764c0, 0x2b322dbfd440 <unfinished ...>
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x16353b0, 0, 0x7ffcfdb57db4, 0x16764c0) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x16353b0, 1, 0x7ffcfdb57db8, 0x2b322e7e2fb4) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x15d9760, 0x16353b0, 0, 0x7ffcfdb57dbc) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x16357e0, 0, 0x7ffcfdb57db4, 7)         = 0
<... hsa_amd_agent_iterate_memory_pools resumed> )                                      = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x15e11e0, 0x16353b0, 0, 0x7ffcfdb57ee0) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x15fd090, 0x16353b0, 0, 0x7ffcfdb57ee0) = 0
libamdhip64.so.3->hsa_amd_agent_memory_pool_get_info(0x1618f40, 0x16353b0, 0, 0x7ffcfdb57ee0) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x16357e0, 2, 0x7ffcfdb57e78, 0x1676cf0) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x16353b0, 2, 0x7ffcfdb57f60, 0x2b322e7e2fb4) = 0
libamdhip64.so.3->hsa_amd_memory_pool_get_info(0x16353b0, 6, 0x1676ae0, 100)            = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 8, 0x7ffcfdb57e5c, 0x2b322e7e2fb4)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 7, 0x7ffcfdb57e6a, 0x2b322e7e2fb4)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 21, 0x7ffcfdb57e54, 0)                  = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 22, 0x7ffcfdb57e56, 0)                  = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 20, 0x7ffcfdb57ee0, 0x1676f00)          = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 0x300b, 0x16765f0, 0x16771f0)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 0x3009, 0x16765a0, 0x16771f0)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 0x300a, 0x16765a8, 0x16771f0)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 0x3003, 0x7ffcfdb57e90, 0x16771f0 <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x1634d50, 0x3003, 0x7ffcfdb57e90, 0x16771f0) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 0x3007, 0x7ffcfdb57e90, 0x7ffcfdb57b6c <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x1634d50, 0x3007, 0x7ffcfdb57e90, 0x7ffcfdb57b6c) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 0x3008, 0x7ffcfdb57e64, 0x7ffcfdb57b6c <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x1634d50, 0x3008, 0x7ffcfdb57e64, 0x7ffcfdb57b6c) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 0x3002, 0x7ffcfdb57e90, 0x7ffcfdb57b6c <unfinished ...>
libhsa-runtime64.so.1->hsa_amd_image_get_info_max_dim(0x1634d50, 0x3002, 0x7ffcfdb57e90, 0x7ffcfdb57b6c) = 0
<... hsa_agent_get_info resumed> )                                                      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 6, 0x167682c, 0x7ffcfdb57b6c)           = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 0xa007, 0x1676590, 0x7ffcfdb57b6c)      = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 0xa00a, 0x7ffcfdb57e60, 0x7ffcfdb57b6c) = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 18, 0x7ffcfdb57e90, 0x7ffcfdb57b6c)     = 0
libamdhip64.so.3->hsa_agent_get_info(0x1634d50, 0xa012, 0x7ffcfdb57e64, 0x7ffcfdb57b6c) = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x15c2c40, 160, 0, 0x7ffcfdb57ec8 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(0, 4096, 64, 0x7ffcfdb57de8)                   = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(4, 0x1652b00, 0, 0x2b322ce8e000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b322ce8e000, 0x7ffcfdb57c80, 0, 0x2b322e1a7160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b322ce8e000, 4096, 0x7ffcfdb57d88, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x15d9d30, 0x101000, 0, 0x7ffcfdb58048 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(3, 0x101000, 8256, 0x7ffcfdb57f68)             = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(4, 0x1652b00, 0, 0x2b3236e00000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b3236e00000, 0x7ffcfdb57e00, 0, 0x2b322e1a7160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b3236e00000, 0x101000, 0x7ffcfdb57f08, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x15d9d30, 0x101000, 0, 0x7ffcfdb58048 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(3, 0x101000, 8256, 0x7ffcfdb57f68)             = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(4, 0x1652b00, 0, 0x2b3237000000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b3237000000, 0x7ffcfdb57e00, 0, 0x2b322e1a7160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b3237000000, 0x101000, 0x7ffcfdb57f08, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_signal_create(1, 0, 0, 0x1676ad0 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtCreateEvent(0x7ffcfdb58030, 0, 0, 0x7ffcfdb58020)          = 0
<... hsa_signal_create resumed> )                                                       = 0
[detect_cuda_device] Querying CUDA devices:
[detect_cuda_device]   Device 0 Device 66a1, CUDA cores 128, global memory size 16368 MB, compute capability 9.0.
[detect_cuda_device]   Device 1 Device 66a1, CUDA cores 128, global memory size 16368 MB, compute capability 9.0.
[detect_cuda_device]   Device 2 Device 66a1, CUDA cores 128, global memory size 16368 MB, compute capability 9.0.
[detect_cuda_device]   Device 3 Device 66a1, CUDA cores 128, global memory size 16368 MB, compute capability 9.0.
[detect_cuda_device] Using CUDA device 0, global memory size 16368 MB.
[aln_core] Loading BWTs, please wait..
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x15e1840, 0x459900, 0, 0x7ffcfdb58118 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(4, 0x600000, 8385, 0x7ffcfdb58038)             = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b3237600000, 0x600000, 0x7ffcfdb58038, 0) = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(3, 0x16534c0, 0, 0x2b3237600000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b3237600000, 0x7ffcfdb57ed0, 0, 0x2b322e1a7160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b3237600000, 0x600000, 0x7ffcfdb57fd8, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x15e1840, 0x459900, 0, 0x7ffcfdb58118 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(4, 0x600000, 8385, 0x7ffcfdb58038)             = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b3644400000, 0x600000, 0x7ffcfdb58038, 0) = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(3, 0x16534c0, 0, 0x2b3644400000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b3644400000, 0x7ffcfdb57ed0, 0, 0x2b322e1a7160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b3644400000, 0x600000, 0x7ffcfdb57fd8, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_executable_create_alt(1, 0, 0, 0x167b0e0)                         = 0
libamdhip64.so.3->hsa_code_object_reader_create_from_memory(0x42064d, 0x15f88, 0x167b0e8, 0x2b364003bd00) = 0
libamdhip64.so.3->hsa_executable_load_agent_code_object(0x1690660, 0x15e11e0, 0x1690870, 0 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(0, 0x12000, 64, 0x7ffcfdb571c8)                = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b322d000000, 0x12000, 0x7ffcfdb571c8, 0) = 0
<... hsa_executable_load_agent_code_object resumed> )                                   = 0
libamdhip64.so.3->hsa_executable_freeze(0x1690660, 0, 0x16a6fc8, 1)                     = 0
libamdhip64.so.3->hsa_executable_get_symbol_by_name(0x1690660, 0x16b57b8, 0x7ffcfdb57978, 0x7ffcfdb57970) = 0
libamdhip64.so.3->hsa_executable_symbol_get_info(0x16b5c80, 22, 0x16aa980, 0x16b7300)   = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 6, 0x7ffcfdb57988, 0x2b322e7e4ea4)      = 0
libamdhip64.so.3->hsa_executable_get_symbol_by_name(0x1690660, 0x1690988, 0x7ffcfdb57978, 0x7ffcfdb57970) = 0
libamdhip64.so.3->hsa_executable_symbol_get_info(0x16b5e80, 22, 0x16b7710, 0x16b7760)   = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 6, 0x7ffcfdb57988, 0x2b322e7e4ea4)      = 0
libamdhip64.so.3->hsa_executable_get_symbol_by_name(0x1690660, 0x16b7788, 0x7ffcfdb57978, 0x7ffcfdb57970) = 0
libamdhip64.so.3->hsa_executable_symbol_get_info(0x16b6090, 22, 0x16b7aa0, 0x16b6bc0)   = 0
libamdhip64.so.3->hsa_agent_get_info(0x15e11e0, 6, 0x7ffcfdb57988, 0x2b322e7e4ea4)      = 0
libamdhip64.so.3->hsa_executable_get_symbol_by_name(0x1690660, 0x153aa48, 0x7ffcfdb58298, 0x7ffcfdb582a0) = 0
libamdhip64.so.3->hsa_executable_symbol_get_info(0x16b65d0, 0, 0x7ffcfdb58294, 0x1679e00) = 0
libamdhip64.so.3->hsa_executable_symbol_get_info(0x16b65d0, 9, 0x1690950, 0x7ffcfdb58294) = 0
libamdhip64.so.3->hsa_executable_symbol_get_info(0x16b65d0, 21, 0x1690948, 0x2b322e7e4f00) = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x15e1840, 0x459900, 0, 0x7ffcfdb58118 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(4, 0x600000, 8385, 0x7ffcfdb58038)             = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b3644c00000, 0x600000, 0x7ffcfdb58038, 0) = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(3, 0x16534c0, 0, 0x2b3644c00000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b3644c00000, 0x7ffcfdb57ed0, 0, 0x2b322e1a7160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b3644c00000, 0x600000, 0x7ffcfdb57fd8, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x15e1840, 0x459900, 0, 0x7ffcfdb58118 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(4, 0x600000, 8385, 0x7ffcfdb58038)             = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b3645400000, 0x600000, 0x7ffcfdb58038, 0) = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(3, 0x16534c0, 0, 0x2b3645400000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b3645400000, 0x7ffcfdb57ed0, 0, 0x2b322e1a7160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b3645400000, 0x600000, 0x7ffcfdb57fd8, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_executable_get_symbol_by_name(0x1690660, 0x153ab08, 0x7ffcfdb58298, 0x7ffcfdb582a0) = 0
libamdhip64.so.3->hsa_executable_symbol_get_info(0x16b67b0, 0, 0x7ffcfdb58294, 0x16b7200) = 0
libamdhip64.so.3->hsa_executable_symbol_get_info(0x16b67b0, 9, 0x167b1b0, 0x7ffcfdb58294) = 0
libamdhip64.so.3->hsa_executable_symbol_get_info(0x16b67b0, 21, 0x167b1a8, 0x2b322e7e4f00) = 0
[aln_core] Finished loading reference sequence assembly, 8 MB in 1.11s (7.18 MB/s).
[aln_core] Sweet! Running with an enlarged buffer for the Tesla/Quadro series.
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x15e1840, 0x800000, 0, 0x7ffcfdb57c38 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(4, 0x800000, 8385, 0x7ffcfdb57b58)             = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b3645c00000, 0x800000, 0x7ffcfdb57b58, 0) = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(3, 0x16534c0, 0, 0x2b3645c00000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b3645c00000, 0x7ffcfdb579f0, 0, 0x2b322e1a7160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b3645c00000, 0x800000, 0x7ffcfdb57af8, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x15e1840, 0x800000, 0, 0x7ffcfdb57c38 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(4, 0x800000, 8385, 0x7ffcfdb57b58)             = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b3646e00000, 0x800000, 0x7ffcfdb57b58, 0) = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(3, 0x16534c0, 0, 0x2b3646e00000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b3646e00000, 0x7ffcfdb579f0, 0, 0x2b322e1a7160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b3646e00000, 0x800000, 0x7ffcfdb57af8, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x15e1840, 88, 0, 0x7ffcfdb57c38)        = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(3, 0x16534c0, 0, 0x2b323d81a000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b323d81a000, 0x7ffcfdb579f0, 0, 0x2b322e1a7160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b323d800000, 0x200000, 0x7ffcfdb57af8, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_executable_get_symbol_by_name(0x1690660, 0x153abd8, 0x7ffcfdb57db8, 0x7ffcfdb57dc0) = 0
libamdhip64.so.3->hsa_executable_symbol_get_info(0x16b66c0, 0, 0x7ffcfdb57db4, 0x167aa00) = 0
libamdhip64.so.3->hsa_executable_symbol_get_info(0x16b66c0, 9, 0x16a9b90, 0x7ffcfdb57db4) = 0
libamdhip64.so.3->hsa_executable_symbol_get_info(0x16b66c0, 21, 0x16a9b88, 0x2b322e7e4f00) = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x15e1840, 0x2b000000, 0, 0x7ffcfdb57c38 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(4, 0x2b000000, 8385, 0x7ffcfdb57b58)           = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b3648000000, 0x2b000000, 0x7ffcfdb57b58, 0) = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(3, 0x16534c0, 0, 0x2b3648000000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b3648000000, 0x7ffcfdb579f0, 0, 0x2b322e1a7160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b3648000000, 0x2b000000, 0x7ffcfdb57af8, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x15e1840, 0x80000, 0, 0x7ffcfdb57bb8)   = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(3, 0x16534c0, 0, 0x2b323d81b000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b323d81b000, 0x7ffcfdb57970, 0, 0x2b322e1a7160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b323d800000, 0x200000, 0x7ffcfdb57a78, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x15e1840, 0x800000, 0, 0x7ffcfdb57bb8 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(4, 0x800000, 8385, 0x7ffcfdb57ad8)             = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b36c9c00000, 0x800000, 0x7ffcfdb57ad8, 0) = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(3, 0x16534c0, 0, 0x2b36c9c00000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b36c9c00000, 0x7ffcfdb57970, 0, 0x2b322e1a7160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b36c9c00000, 0x800000, 0x7ffcfdb57a78, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0
[aln_core] Now aligning sequence reads to reference assembly, please wait..
[aln_core] Processing 67584 sequence reads at a time.
[aln_core] cuda_inexact_match_caller...libamdhip64.so.3->hsa_amd_memory_pool_free(0x2b323d81b000, 0x2b323d81b000, 0x80000, 0)  = 0
libamdhip64.so.3->hsa_amd_memory_pool_free(0x2b36c9c00000, 0x2b36c9c00000, 0x800000, 0 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtUnmapMemoryToGPU(0x2b36c9c00000, 0x2b36c9c00000, 0x2b364003a520, 0x15e18e0) = 0
libhsa-runtime64.so.1->hsaKmtFreeMemory(0x2b36c9c00000, 0x800000, 0x2b3235b923f8, 0x16aa300) = 0
<... hsa_amd_memory_pool_free resumed> )                                                = 0
libamdhip64.so.3->hsa_amd_memory_pool_allocate(0x15e1840, 0x800000, 0, 0x7ffcfdb57bb8 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtAllocMemory(4, 0x800000, 8385, 0x7ffcfdb57ad8)             = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b36c9200000, 0x800000, 0x7ffcfdb57ad8, 0) = 0
<... hsa_amd_memory_pool_allocate resumed> )                                            = 0
libamdhip64.so.3->hsa_amd_agents_allow_access(3, 0x16534c0, 0, 0x2b36c9200000 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtQueryPointerInfo(0x2b36c9200000, 0x7ffcfdb57970, 0, 0x2b322e1a7160) = 0
libhsa-runtime64.so.1->hsaKmtMapMemoryToGPUNodes(0x2b36c9200000, 0x800000, 0x7ffcfdb57a78, 0) = 0
<... hsa_amd_agents_allow_access resumed> )                                             = 0

[aln_core] Finished!
[aln_core] Total no. of sequences: 65536, size in base pair: 2293760 bp, average length 35.00 bp/sequence.
[aln_core] Alignment Speed: 29395.27 sequences/sec or 1028834.62 bp/sec.
[aln_core] Total program time: 2.23s.
libamdhip64.so.3->hsa_amd_memory_pool_free(0x2b3645c00000, 0x2b3645c00000, 0x800000, 0 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtUnmapMemoryToGPU(0x2b3645c00000, 0x2b3645c00000, 0x2b364003a520, 0x15e18e0) = 0
libhsa-runtime64.so.1->hsaKmtFreeMemory(0x2b3645c00000, 0x800000, 0x2b3235b923f8, 0x1679a00) = 0
<... hsa_amd_memory_pool_free resumed> )                                                = 0
libamdhip64.so.3->hsa_amd_memory_pool_free(0x2b3646e00000, 0x2b3646e00000, 0x800000, 0 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtUnmapMemoryToGPU(0x2b3646e00000, 0x2b3646e00000, 0x2b364003a520, 0x15e18e0) = 0
libhsa-runtime64.so.1->hsaKmtFreeMemory(0x2b3646e00000, 0x800000, 0x2b3235b923f8, 0x16a9300) = 0
<... hsa_amd_memory_pool_free resumed> )                                                = 0
libamdhip64.so.3->hsa_amd_memory_pool_free(0x2b3648000000, 0x2b3648000000, 0x2b000000, 0 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtUnmapMemoryToGPU(0x2b3648000000, 0x2b3648000000, 0x2b364003a520, 0x15e18e0) = 0
libhsa-runtime64.so.1->hsaKmtFreeMemory(0x2b3648000000, 0x2b000000, 0x2b3235b923f8, 0x16a9800) = 0
<... hsa_amd_memory_pool_free resumed> )                                                = 0
libamdhip64.so.3->hsa_amd_memory_pool_free(0x2b3644400000, 0x2b3644400000, 0x459900, 0 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtUnmapMemoryToGPU(0x2b3644400000, 0x2b3644400000, 0x2b364003a520, 0x15e18e0) = 0
libhsa-runtime64.so.1->hsaKmtFreeMemory(0x2b3644400000, 0x600000, 0x2b3235b923f8, 0x1679e00) = 0
<... hsa_amd_memory_pool_free resumed> )                                                = 0
libamdhip64.so.3->hsa_amd_memory_pool_free(0x2b3237600000, 0x2b3237600000, 0x459900, 0 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtUnmapMemoryToGPU(0x2b3237600000, 0x2b3237600000, 0x600000, 0x2b364003a4f0) = 0
libhsa-runtime64.so.1->hsaKmtFreeMemory(0x2b3237600000, 0x600000, 0x2b3235b923f8, 0x1679000) = 0
<... hsa_amd_memory_pool_free resumed> )                                                = 0
libamdhip64.so.3->hsa_amd_memory_pool_free(0x2b3645400000, 0x2b3645400000, 0x459900, 0 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtUnmapMemoryToGPU(0x2b3645400000, 0x2b3645400000, 0x2b364003a520, 0x15e18e0) = 0
libhsa-runtime64.so.1->hsaKmtFreeMemory(0x2b3645400000, 0x600000, 0x2b3235b923f8, 0x16b7200) = 0
<... hsa_amd_memory_pool_free resumed> )                                                = 0
libamdhip64.so.3->hsa_amd_memory_pool_free(0x2b3644c00000, 0x2b3644c00000, 0x459900, 0 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtUnmapMemoryToGPU(0x2b3644c00000, 0x2b3644c00000, 0x2b364003a520, 0x15e18e0) = 0
libhsa-runtime64.so.1->hsaKmtFreeMemory(0x2b3644c00000, 0x600000, 0x2b3235b923f8, 0x16b7200) = 0
<... hsa_amd_memory_pool_free resumed> )                                                = 0
libamdhip64.so.3->hsa_executable_destroy(0x1690660, 0x2b322e4e8768, 0xffffffff, 0x14ab400 <unfinished ...>
libhsa-runtime64.so.1->hsaKmtUnmapMemoryToGPU(0x2b322d000000, 0x2b322d000000, 0x12000, 0x15c2ce0) = 0
libhsa-runtime64.so.1->hsaKmtFreeMemory(0x2b322d000000, 0x12000, 0x2b3235b923f8, 0x16b5900) = 0
<... hsa_executable_destroy resumed> )                                                  = 0
libamdhip64.so.3->hsa_code_object_reader_destroy(0x1690870, 0, 0x1651480, 0x1690650)    = 0
disable_breakpoint pid=11385744, addr=0x2b323597b4e0: No such process
PTRACE_SINGLESTEP: No such process
11385744 couldn't continue when handling hsaKmtWaitOnMultipleEvents (0x2b323597b4e0) at 0xffffffffffffffff
disable_breakpoint pid=16747, addr=0x2b323597b4e0: No such process
+++ exited (status 0) +++
</details>

Thanks!
Merry Christmas!






---

### 评论 #5 — ROCmSupport (2021-01-04T07:18:42Z)

@bearwithdog ,

     Happy new year :)
     The delayed reply is because of vacation.
 
     Thank you for posting the project.
     We are still clueless about the topology of the hardware you are using hence, I request you to kindly post the output of


```
      /opt/rocm/bin/rocminfo
      /opt/rocm/bin/rocm-bandwidth-test -t
      /opt/rocm/bin/rocm-bandwidth-test
```

      for better reproducibility of the problem faced by you, Although we shall still try to get the problem reproduced & fixed.
 

---

### 评论 #6 — ROCmSupport (2021-01-05T10:24:19Z)

@bearwithdog,

    Your code is specific to CentOS; Further, it does not compiles on Debian because of hardcoding of the OS specific things in makefiles & code. 
    Could you kindly make your code which works for either COS 8.x or Debian?
    Also, we need the output for the above commands as asked earlier.

    BTW, if you could try to check the problem you reported is still observable on latest release ROCm 4.0, it could save efforts both for you & us.

    Thanks

---

### 评论 #7 — bearwithdog (2021-01-06T02:21:13Z)

@ROCmSupport
1.The output of commands as follows.
<details>
<summary>/opt/rocm/bin/rocminfo</summary>
<pre><code>
ROCk module is loaded
Able to open /dev/kfd read-write
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz
  Uuid:                    CPU-XX                             
  Marketing Name:          Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2101                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            32                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    65462236(0x3e6dfdc) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    65462236(0x3e6dfdc) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 2                  
*******                  
  Name:                    Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz
  Uuid:                    CPU-XX                             
  Marketing Name:          Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   2101                               
  BDFID:                   0                                  
  Internal Node ID:        1                                  
  Compute Unit:            32                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    66026728(0x3ef7ce8) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    66026728(0x3ef7ce8) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
    N/A                      
*******                  
Agent 3                  
*******                  
  Name:                    gfx900                             
  Uuid:                    GPU-02163643d1562944               
  Marketing Name:          Vega 10 [Radeon Instinct MI25]     
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    2                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 26720(0x6860)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1500                               
  BDFID:                   15616                              
  Internal Node ID:        2                                  
  Compute Unit:            64                                 
  SIMDs per CU:            4                                  
  Shader Engines:          4                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        40(0x28)                           
  Max Work-item Per CU:    2560(0xa00)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16760832(0xffc000) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx900          
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
*******                  
Agent 4                  
*******                  
  Name:                    gfx900                             
  Uuid:                    GPU-02163643d1564924               
  Marketing Name:          Vega 10 [Radeon Instinct MI25]     
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    3                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 26720(0x6860)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1500                               
  BDFID:                   34816                              
  Internal Node ID:        3                                  
  Compute Unit:            64                                 
  SIMDs per CU:            4                                  
  Shader Engines:          4                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        40(0x28)                           
  Max Work-item Per CU:    2560(0xa00)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16760832(0xffc000) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx900          
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
*** Done ***             
</code></pre>
</details>
 
<details>
<summary>/opt/rocm/bin/rocm-bandwidth-test -t</summary>
<pre><code>
RocmBandwidthTest Version: 2.4.0

Launch Command is: rocm-bandwidth-test -t


Device Index:                             0
  Device Type:                            CPU
  Device Name:                            Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz
    Allocatable Memory Size (KB):         65462236

Device Index:                             1
  Device Type:                            CPU
  Device Name:                            Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz
    Allocatable Memory Size (KB):         66026728

Device Index:                             2
  Device Type:                            GPU
  Device Name:                            Vega 10 [Radeon Instinct MI25]
  Device  BDF:                            3d:0.0
    Allocatable Memory Size (KB):         16760832

Device Index:                             3
  Device Type:                            GPU
  Device Name:                            Vega 10 [Radeon Instinct MI25]
  Device  BDF:                            88:0.0
    Allocatable Memory Size (KB):         16760832


Inter-Device Access

D/D       0         1         2         3         

0         1         1         0         0         

1         1         1         0         0         

2         1         1         1         0         

3         1         1         0         1         


Inter-Device Link Type: P = PCIe, X = xGMI, N/A = Not Applicable

D/D       0         1         2         3         

0         N/A       N/A       N/A       N/A       

1         N/A       N/A       N/A       N/A       

2         P         P         N/A       N/A       

3         P         P         N/A       N/A       


Inter-Device Numa Distance

D/D       0         1         2         3         

0         0         21        N/A       N/A       

1         21        0         N/A       N/A       

2         20        41        0         N/A       

3         41        20        N/A       0       
</code></pre>
</details> 

<details>
<summary>/opt/rocm/bin/rocm-bandwidth-test</summary>
<pre><code>
............................
RocmBandwidthTest Version: 2.4.0

Launch Command is: rocm-bandwidth-test (rocm_bandwidth -a + rocm_bandwidth -A)


Device: 0,  Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz
Device: 1,  Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz
Device: 2,  Vega 10 [Radeon Instinct MI25],  3d:0.0
Device: 3,  Vega 10 [Radeon Instinct MI25],  88:0.0

Inter-Device Access

D/D       0         1         2         3         

0         1         1         0         0         

1         1         1         0         0         

2         1         1         1         0         

3         1         1         0         1         


Inter-Device Numa Distance

D/D       0         1         2         3         

0         0         21        N/A       N/A       

1         21        0         N/A       N/A       

2         20        41        0         N/A       

3         41        20        N/A       0         


Unidirectional copy peak bandwidth GB/s

D/D       0           1           2           3           

0         N/A         N/A         13.682077   13.695748   

1         N/A         N/A         13.813928   13.826172   

2         14.287556   14.282596   354.577134  N/A         

3         14.286218   14.283067   N/A         353.885311  


Bdirectional copy peak bandwidth GB/s

D/D       0           1           2           3           

0         N/A         N/A         25.878974   25.764196   

1         N/A         N/A         25.896730   25.899718   

2         25.878974   25.896730   N/A         N/A         

3         25.764196   25.899718   N/A         N/A 
</code></pre>
</details>

2. lsb_release -a
LSB Version:	:core-4.1-amd64:core-4.1-noarch:cxx-4.1-amd64:cxx-4.1-noarch:desktop-4.1-amd64:desktop-4.1-noarch:languages-4.1-amd64:languages-4.1-noarch:printing-4.1-amd64:printing-4.1-noarch
Distributor ID:	CentOS
Description:	CentOS Linux release 7.6.1810 (Core) 
Release:	7.6.1810
Codename:	Core

Upgrading the operating system version is a bit difficult.Is it necessary for me to use docker for testing?

3.There's still a problem when I tested the code on rocm-4.0.

4.I found a similar problem which like "Device::callbackQueue aborting with status: 0x29"
https://github.com/RadeonOpenCompute/ROCm/issues/1220

That's the information I've provided.
Thanks for your patience.
BTW,I have multiple rocm environments and I use module to manage.



---

### 评论 #8 — ROCmSupport (2021-01-06T07:24:36Z)

Hi @bearwithdog, 
    Thanks for the command output. We shall check with your hardware config for the problem.

---

### 评论 #9 — ROCmSupport (2021-01-07T12:34:49Z)

@bearwithdog,
  In your system, it appears that your GPUs do not have Peer2Peer enabled. could you kindly do the following :

     1) cd /opt/rocm/hip/samples/2_Cookbook/8_peer2peer
     2) sudo make 

 If this gives you output : 
    
          ./peer2peer
          currentGpu#1 canAccessPeer: peerGpu#0=1
           currentGpu=0 peerGpu=1 (Total no. of gpu = 2)
           Peer2Peer PASSED!

 if enabled, but in your case, it should fail 

           FAILED:  errors 

if it does, then, I would suggest you to try to enable peer2peer from your bios settings & then try your test case.

Let me know if this helps.

---

### 评论 #10 — bearwithdog (2021-01-08T06:04:35Z)

@ROCmSupport
Thanks a lot.
./peer2peer 
currentGpu#1 canAccessPeer: peerGpu#0=0
currentGpu=0 peerGpu=1 (Total no. of gpu = 2)
peer2peer transfer not possible between the selected gpu devicespeer2peer disable not requiredPeer2Peer PASSED!

That is command output.It's a little differents from yours.I'm not sure if this is enable already.


---

### 评论 #11 — ROCmSupport (2021-01-08T06:16:28Z)

@bearwithdog,
Waiting for your update on the above suggestion ( _changing to peer2peer & then execute the test_ ) . 
Also, I tried to repro but, nothing seems to be moving & there is a state of freeze & not logs  are coming.
With GDB I came to know that your code is stuck in while loop 

       0x000000000040f7eb in aln_quicksort (aln=0x7f502709b010, m=0, n=1935892556) at bwase.c:83
       83                       while((i <= n) && (aln[i].score <= key))
       Missing separate debuginfos, use: debuginfo-install elfutils-libelf-0.176-5.el7.x86_64 glibc-2.17-317.el7.x86_64 libgcc-4.8.5-44.el7.x86_64


Till now I did not witness the problem you reported. Is there something I am missing here?

Please find my logs below :

[GDB_logs.txt](https://github.com/RadeonOpenCompute/ROCm/files/5785504/GDB_logs.txt)
[Repro_logs.txt](https://github.com/RadeonOpenCompute/ROCm/files/5785506/Repro_logs.txt)


---

### 评论 #12 — bearwithdog (2021-01-08T07:40:12Z)

@ROCmSupport
em....em,I need some  time to understand logs.
My environment is shared by many people.Maybe, I shoule use docker to testing it .
it puzzle me. @_@
Thank you for your support.
I will continue to follow up and if I have any new developments or fix it, I will update.





---

### 评论 #13 — ROCmSupport (2021-01-28T06:50:21Z)

Hi @bearwithdog 
Any update on this?
Thank you.

---

### 评论 #14 — ROCmSupport (2021-02-02T09:56:21Z)

@bearwithdog ,  We are closing this currently. Kindly check the suggestion posted & if you still have problem kindly let us know with new issue

---

### 评论 #15 — mathmax12 (2021-05-23T01:00:23Z)

> enable peer2peer from your bios

I am facing the same issue recently. when I check the peer2peer I got:
`/opt/rocm/hip/bin/hipcc -g   -c -o peer2peer.o peer2peer.cpp
make: /opt/rocm/hip/bin/hipcc: Command not found
<builtin>: recipe for target 'peer2peer.o' failed
make: *** [peer2peer.o] Error 127`

I wonder how to enable it?
Thanks

---
