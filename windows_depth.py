import pandas as pd

def get_windows_depths(in_depth, win_size=9):
  
  out_depth = in_depth.replace('.depth', '.window.depth')
  total_depth = 0
  c = 0
  ave_depths = {}
  with open(in_depth, 'r') as f:
    for line in f:
      c += 1
      seq = line.split()[0]
      pos = int(line.split()[1])
      depth = int(line.split()[2])
      total_depth += depth
      if c >= win_size:
        mean_depth = total_depth/win_size
        max_pos = pos
        ave_depths[max_pos] = mean_depth
        #print(f"{max_pos} {mean_depth}")
        total_depth = 0
        c = 0
  
  # # if position from last line is greater than max_pos, 
  # # that means we have some lines that weren`t included 
  # # in the average depth calculation because they were after
  # # the last window. 
  # if pos > max_pos:
  #   for i in range(max_pos+1, pos+1):
  #     with open()    

  with open(out_depth, "w") as f2:
    for ref_position, depth in ave_depths.items():
      for i in range(ref_position-win_size+1,ref_position+1):
        #print("\t".join(seq, i, depth))       
        f2.write("\t".join([seq, str(i), str(depth)]) + "\n")


def windows_to_base(depth_per_windows, seq_ID):
  out_filename = f"{seq_ID}.mean.perBase.depth"
  print(f"Transfer mean depth values from windows ({depth_per_windows}) to base system ({out_filename})")
  with open(depth_per_windows, "r") as f:
    for window in f:
      #seq = window.split()[0]
      min_pos = int(window.split()[1])
      max_pos = int(window.split()[2])
      raw_depth = float(window.split()[3])
      rounded_depth = f"{raw_depth:.2f}"
      for i in range(min_pos+1, max_pos+1):
        with open(out_filename, "a") as f2:
          f2.write("\t".join([str(i), rounded_depth]) + "\n")
  return out_filename

def windows_to_base_df(depth_per_windows, seq_ID):
  #out_filename = f"{seq_ID}.mean.perBase.depth"
  #print(f"Transfer mean depth values from windows ({depth_per_windows}) to base system ({out_filename})")
  df = pd.DataFrame(columns=['position', 'depth'])
  with open(depth_per_windows, "r") as f:
    for window in f:
      #seq = window.split()[0]
      min_pos = int(window.split()[1])
      max_pos = int(window.split()[2])
      raw_depth = float(window.split()[3])
      rounded_depth = f"{raw_depth:.2f}"
      for i in range(min_pos+1, max_pos+1):
        data = {'position': i, 'depth': rounded_depth}  
        df = df.append(data, ignore_index=True)
  return df 
