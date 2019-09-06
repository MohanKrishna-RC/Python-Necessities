for episode in episodes:
    audiofile = AudioFileClip(audio_folder+episode)
    for i in range(10):
        if (gt_footsteps_dict[episode][i]==1 and pred_footsteps_dict[episode][i]==1):
            tp += 1
        elif (gt_footsteps_dict[episode][i]==0 and pred_footsteps_dict[episode][i]==1):
            audio_file_name = fp_folder+"/speech_"+str(i)+"_"+str(i+1)+episode
  #          clip.to_audiofile(audio_file_name)
            fp += 1
        elif (gt_footsteps_dict[episode][i]==1 and pred_footsteps_dict[episode][i]==0):
            audio_file_name = fn_folder+"/speech_"+str(i)+"_"+str(i+1)+episode
   #         clip.to_audiofile(audio_file_name)
            fn += 1