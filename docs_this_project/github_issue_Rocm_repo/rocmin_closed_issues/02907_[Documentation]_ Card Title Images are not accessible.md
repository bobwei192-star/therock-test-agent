# [Documentation]: Card Title Images are not accessible

- **Issue #:** 2907
- **State:** closed
- **Created:** 2024-02-19T09:33:17Z
- **Updated:** 2024-08-13T23:02:56Z
- **Labels:** Documentation
- **URL:** https://github.com/ROCm/ROCm/issues/2907

### Description of errors

The titles for the "cards" are images with text. Alternative text is not provided. This is very bad for screen readers and search engines.

Ideally the text should be in HTML and only the background should be an image. This would also make the site more printer friendly. [Sphinx design allows custom css classes](https://sphinx-design.readthedocs.io/en/latest/css_classes.html) to be applied to elements that should make this fairly straightforward
At the very least description of these images need to be provided.

As an extra comment these images are quite large raster images, it would be nice to replace them with vector if possible graphics with smaller size.

### Attach any links, screenshots, or additional evidence you think will be helpful.

![image](https://github.com/ROCm/ROCm/assets/8176760/421121d1-894d-4553-b361-720f61527a46)
![image](https://github.com/ROCm/ROCm/assets/8176760/eb664ed1-c4d1-4695-8c35-9fe3b0ca5c6d)
