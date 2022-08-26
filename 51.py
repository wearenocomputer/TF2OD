import fiftyone as fo
import fiftyone.zoo as foz

#dataset = foz.load_zoo_dataset("quickstart")


dataset = foz.load_zoo_dataset(
               "open-images-v6",
               split="train",
               label_types=["detections"],
               classes=["Skateboard", "Guitar","Bottle","Mug","Stapler","Tin can"],
               max_samples=18000,
          )

session = fo.launch_app(dataset)


#import fiftyone as fo
#import fiftyone.zoo as foz
#dataset = foz.load_zoo_dataset(
#    "open-images-v6", 
#    split="validation", 
#    max_samples=100
#)

#session = fo.launch_app(dataset)