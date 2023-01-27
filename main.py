import os
import sys
import traceback

version = '1.0'
cur_dir = os.getcwd()

#譜面合成後に出力するファイルの初期化
with open(f"{cur_dir}/connected.sus", mode='w') as f:
    f.write(f"This file was connected by sus-connector {version}\n")

try:

    score_lines = []

    #読み取った譜面情報を統合
    for i in range(1, len(sys.argv)):
        file = sys.argv[i]
        ext = os.path.splitext(file)
        with open(file) as f:
            lines = f.readlines()
            #print(f"{lines}\n")
            score_lines.extend(lines)

    #print(score_lines)
    #print("\n")

    #譜面情報の書き込み
    with open(f"{cur_dir}/connected.sus", mode='a') as f:
        new_score_lines = list(dict.fromkeys(score_lines))
        f.writelines(new_score_lines)

except Exception as e:
    ty, v, tr = sys.exc_info()
    print(traceback.format_exception(ty, v, tr))
    print("エラーが発生しました。")
    input("")

