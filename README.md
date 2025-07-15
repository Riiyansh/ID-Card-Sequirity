[![Live App](https://img.shields.io/badge/View-Live--Demo-brightgreen?style=for-the-badge)](https://minor-project-klmh.onrender.com)

# Document Verification System using Image Similarity


## Overview
<img width="1499" alt="Screenshot 2025-05-02 at 10 28 27 AM" src="https://github.com/user-attachments/assets/5b4cd61c-f2e5-4351-a361-6ef7579dc473" />

<img width="1501" alt="Screenshot 2025-05-02 at 10 28 34 AM" src="https://github.com/user-attachments/assets/8ed41a96-c353-4b52-88d0-27508cf0fa3e" />
<img width="1502" alt="Screenshot 2025-05-02 at 10 28 19 AM" src="https://github.com/user-attachments/assets/8a00447a-d693-476c-8c29-297f803d0195" />


This project is designed to detect tampering of ID cards using computer vision techniques. It helps organizations verify the authenticity of PAN cards provided by employees, customers, or any other individuals. The project achieves this by calculating the structural similarity between an original PAN card and a user-provided PAN card image.

## Project Workflow

1. **Image Loading and Preprocessing:**
   - The original PAN card image and the user-provided PAN card image are loaded.
   - Images are resized and formatted to ensure consistency in comparison.

2. **Structural Similarity Index (SSIM):**
   - The structural similarity between the original and user-provided images is calculated. SSIM helps in identifying the degree of similarity between two images.
   - A lower SSIM score indicates a higher likelihood of tampering.

3. **Thresholding and Contour Detection:**
   - The difference between the images is converted to a binary format using thresholding.
   - Contours are identified to locate the areas of difference between the two images.

4. **Visualization:**
   - The project visualizes the original image, tampered image, difference image, and the threshold image to highlight the areas where tampering may have occurred.

## Prerequisites

To run this project, you need the following libraries installed:

- `skimage`
- `imutils`
- `opencv-python`
- `Pillow`
- `requests`

You can install these using pip:

```bash
pip install scikit-image imutils opencv-python Pillow requests
```

## How to Use

1. Clone this repository to your local machine.
2. Ensure you have the necessary Python packages installed.
3. Run the script `pan_card_tampering_detection.py`.
4. The program will load the images, process them, and display the results, including the SSIM score and visualizations of the differences.

## Example Output

- **SSIM Score:** A score indicating the similarity between the original and tampered image. A low score (e.g., ~31.2%) suggests significant tampering.
- **Visualization:** Images with highlighted contours showing the differences between the original and tampered images.

## Applications

- **Identity Verification:** This project can be used by organizations to verify the authenticity of PAN cards provided by users.
- **Tampering Detection for Other IDs:** The methodology can be extended to detect tampering in other types of identity documents, such as Aadhar cards, voter IDs, etc.

## Future Scope

- **Enhancing Accuracy:** Improving the SSIM threshold and integrating additional image processing techniques for better accuracy.
- **Expanding to Other Documents:** Adapting the system to work with other government-issued ID cards.
- **Automated System Integration:** Deploying the solution in real-time systems used by organizations for automated ID verification.

## Conclusion

This project provides a simple yet effective method for detecting tampering in PAN cards using computer vision. By analyzing structural similarity and visualizing differences, it helps ensure the authenticity of identity documents.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```


