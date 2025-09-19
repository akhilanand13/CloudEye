import boto3
import csv

# 1. AWS Configuration

region = "us-east-1"
bucket_name = "<my-bucket-name>"

rekognition = boto3.client('rekognition', region_name=region)
s3 = boto3.client('s3', region_name=region)

# 2. Function to detect labels

def detect_labels(bucket, image_name, max_labels=10, min_confidence=80):
    try:
        response = rekognition.detect_labels(
            Image={'S3Object': {'Bucket': bucket, 'Name': image_name}},
            MaxLabels=max_labels,
            MinConfidence=min_confidence
        )

        labels_info = []
        for label in response['Labels']:
            labels_info.append((label['Name'], round(label['Confidence'], 2)))
        
        return labels_info

    except Exception as e:
        print(f"Error detecting labels for {image_name}: {e}")
        return []
        
# 3. Get all images from the bucket

try:
    objects = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in objects:
        image_files = [obj['Key'] for obj in objects['Contents'] if obj['Key'].lower().endswith(('.jpg', '.jpeg', '.png'))]
        print("Images found in bucket:", image_files)
    else:
        print("No images found in the bucket.")
        image_files = []
except Exception as e:
    print(f"Error listing bucket contents: {e}")
    image_files = []

# 4. Detect labels and save to CSV

csv_file = "rekognition_labels.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Image Name", "Label", "Confidence"])
    for image in image_files:
        labels = detect_labels(bucket_name, image)
        if labels:
            print(f"Labels detected for {image}:")
            for name, confidence in labels:
                print(f"{name} : {confidence}%")
                writer.writerow([image, name, confidence])
            print("-----------------------------")
print(f"\nAll detected labels have been saved to {csv_file}")

