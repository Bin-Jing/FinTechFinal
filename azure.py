import requests
# If you are using a Jupyter notebook, uncomment the following line.
#%matplotlib inline
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
from io import BytesIO

# Replace <Subscription Key> with your valid subscription key.
subscription_key = ""
assert subscription_key

# You must use the same region in your REST call as you used to get your
# subscription keys. For example, if you got your subscription keys from
# westus, replace "westcentralus" in the URI below with "westus".
#
# Free trial subscription keys are generated in the "westus" region.
# If you use a free trial subscription key, you shouldn't need to change
# this region.
vision_base_url = "https://australiaeast.api.cognitive.microsoft.com/vision/v1.0/"

ocr_url = vision_base_url + "ocr"

image_path = "aaa.jpg"

# Read the image into a byte array
image_data = open(image_path, "rb").read()
headers    = {'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/octet-stream'}
params     = {'language': 'en', 'detectOrientation': 'true','visualFeatures': 'Categories,Description,Color'}
response = requests.post(
                         ocr_url, headers=headers, params=params, data=image_data)
response.raise_for_status()
## Set image_url to the URL of an image that you want to analyze.
#image_path = "img.jpg"
#
#image_data = open(image_path, "rb").read()
#headers = {'Ocp-Apim-Subscription-Key': subscription_key}
#params  = {'language': 'unk', 'detectOrientation': 'true'}
#response = requests.post(ocr_url, headers=headers, params=params, data=image_data)
#response.raise_for_status()

analysis = response.json()
print(analysis)
# Extract the word bounding boxes and text.
line_infos = [region["lines"] for region in analysis["regions"]]
word_infos = []
for line in line_infos:
    for word_metadata in line:
        for word_info in word_metadata["words"]:
            word_infos.append(word_info)

print(word_infos)

# Display the image and overlay it with the extracted text.
plt.figure(figsize=(5, 5))
image = Image.open(BytesIO(image_data))
ax = plt.imshow(image, alpha=0.5)
for word in word_infos:
    bbox = [int(num) for num in word["boundingBox"].split(",")]
    text = word["text"]
    origin = (bbox[0], bbox[1])
    patch  = Rectangle(origin, bbox[2], bbox[3], fill=False, linewidth=2, color='y')
    ax.axes.add_patch(patch)
    plt.text(origin[0], origin[1], text, fontsize=20, weight="bold", va="top")
plt.axis("off")
