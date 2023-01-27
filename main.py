import os
import sys
import traceback

version = '1.1'
cur_dir = os.getcwd()

#譜面合成後に出力するファイルの初期化
with open(f"{cur_dir}/connected.sus", mode='w') as f:
    f.write(f"This file was connected by sus-connector {version}\n")

try:

    ext_type = '.sus'
    score_lines = []

    #読み取った譜面情報を統合
    for i in range(1, len(sys.argv)):
        file = sys.argv[i]
        ext = os.path.splitext(file)
        if ext_type == ext[1]:
            with open(file) as f:
                lines = f.readlines()
                score_lines.extend(lines)
        else:
            raise Exception

    #譜面情報の書き込み
    with open(f"{cur_dir}/connected.sus", mode='a') as f:
        new_score_lines = list(dict.fromkeys(score_lines))
        f.writelines(new_score_lines)

except Exception as e:
   traceback.print_exc()
   input("終了するには何かキーを押してください...")

