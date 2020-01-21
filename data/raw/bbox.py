import os, cv2, glob, csv
import pandas as pd
import numpy as np
csv = "/home/mohan/Downloads/3692df67-ab7d-4208-a80d-bc270f9d055a_vmd_features_c6130387-58c6-4893-a09e-99236bec23db_entity_2020012019230002_quality_paramters__encoder_csv_Sportcast_1634.csv"

df = pd.read_csv(csv)
print(df.head())
df = df[df['roi_id'].notnull()]

a = np.unique(df['video_frame_asset_path'])
print((a[0]))
# # input_frames_folder = "/home/aodev/demo_video_rois_and_frames/frames"
for i in range(len(a)):
    b = "output_folder_{}".format(i)
    # print(b)
    b = os.path.join("/home/mohan/demo_testing/",a[i].split('/')[-1].split(".")[0])
    # print(b)
    os.system("gsutil -m cp -r {} ./b".format(a[i]))
    c = b.split('/')[-1]
    # print(c)
    os.system("unzip b -d demo/{}/".format(c))

output_folder = "/home/mohan/demo_testing/exp/"
# csv = "/home/mohan/bbox_test_logo.csv"
# # csv = "/home/aodev/demo_video_rois_and_frames/predictions_18_apr_rois.csv"
input_frames_folder = "/home/mohan/demo_testing/demo/"

for i in range(len(df)):
    
    for image in glob.glob(input_frames_folder+'/*/*'):
        image_name = image.split("/")[-1]
        # print("image name: " , image)
    # image_name_without_ext = image_name.split(".")[0]
        img = cv2.imread(image)
    
        try:
            row = df[i:i+1]
            # if os.path.join(input_frames_folder,df['video_frame_asset_path'][i].split('/')[-1].split('.')[0]) ==  
            if image_name==row.frame_id.to_list()[0]:
                if not row.roi_id.to_list()[0] == "":
                    # print(row)
                    # print(row.roi_id)
                    x1 = int(row.xmax)
                    y1 = int(row.ymax)
                    x2 = int(row.xmin)
                    y2 = int(row.ymin)

                    cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
                    cv2.rectangle(img, (120,96), (600,480), (255,0,0), 2)
                    cv2.rectangle(img, (240,192), (480,384), (255,128,0), 2)

                    print("done")
                    print(img.shape)

                    if not os.path.exists(output_folder + "/" + row.roi_tag_metrics__centrality_overall_tag.item()):
                        os.makedirs(output_folder + "/" + row.roi_tag_metrics__centrality_overall_tag.item())

                    cv2.imwrite(output_folder + "/" + row.roi_tag_metrics__centrality_overall_tag.item() + '/' + row.frame_id.item().split('.')[0] + '_' + row.roi_id.item() + ".jpg",img)
                else:
                    if not os.path.exists(output_folder + "/" + row.roi_tag_metrics__centrality_overall_tag.item()):
                        os.makedirs(output_folder + "/" + row.roi_tag_metrics__centrality_overall_tag.item())

                    cv2.imwrite(output_folder + "/" + row.roi_tag_metrics__centrality_overall_tag.item() + '/' + row.frame_id.item().split('.')[0] + ".jpg",img)
            else:
                continue        
        except Exception as e:
            print(e)
        # cv2.putText(img, text, (x1,y2+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)