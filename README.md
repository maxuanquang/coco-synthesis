# Initial Setup

```
pip install -r requirements.txt
```
# Create Synthetic Images

In this section, we will use "src/image_composition.py" to randomly pick foregrounds and automatically super-impose them on backgrounds. You will need a number of foreground cutouts with transparent backgrounds. For example, you might have a picture of an eagle with a completely transparent background. Due to the need for transparency, these images should be .png format (.jpg doesn't have transparency). I cut out my foregrounds with [GIMP](https://www.gimp.org/), which is free.

- Inside that "dataset" directory, create a folder called "input"
- Inside "input", create two folders called "foregrounds" and "backgrounds"
- Inside "foregrounds", create a folder for each super category (e.g. "bird", "lizard")
- Inside each foreground super category folder, create a folder for each category (e.g. "eagle", "owl")
- Inside each category folder, add all foreground photos you intend to use for the respective category (e.g. all of you eagle foreground cutouts)
- Inside "backgrounds", add all background photos you intend to use

Run "image_composition.py" to create your synthesis images
```
python src/image_composition.py --input_dir dataset/input --output_dir dataset/output --count 10 --width 512 --height 512
```

# Check Output Synthetic Images

- The output sythetic images are in "dataset/output/images"
- The output labels in .xml format for syntheic images are in "dataset/output/xml"
- You can convert .xml format to .csv format using:
```
python src/xml_to_csv.py
```
- You can check quality of output synthetic images using
```
python src/test_xml.py
python src/test_csv.py
```