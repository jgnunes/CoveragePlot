def get_windows_depths(in_depth, win_size=9):
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

  with open("window_depths.out.tsv", "w") as f2:
    for ref_position, depth in ave_depths.items():
      for i in range(ref_position-win_size+1,ref_position+1):
        #print("\t".join(seq, i, depth))       
        f2.write("\t".join([seq, str(i), str(depth)]) + "\n")
