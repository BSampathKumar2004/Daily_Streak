#!/bin/bash

cd /home/criativo/Documents/Coding/Daily_Streak_GitHub/Daily_Streak || exit

export PATH=/usr/bin:/bin:/usr/local/bin

count=$((RANDOM % 6 + 5))

for ((i=1; i<=count; i++))
do
    date=$(date +"%Y-%m-%d %H:%M:%S")

    # better unique filename
    file="code_${i}_$(date +%s%N).txt"

    langs=("py" "c" "cpp" "java" "r")
    lang=${langs[$RANDOM % ${#langs[@]}]}

    case $lang in
        py)
            echo -e "# Python\nprint('Hello $date')" > "${file}.py"
            ;;
        c)
            echo -e "// C\n#include <stdio.h>\nint main(){printf(\"Hello $date\");}" > "${file}.c"
            ;;
        cpp)
            echo -e "// C++\n#include <iostream>\nint main(){std::cout<<\"Hello $date\";}" > "${file}.cpp"
            ;;
        java)
            echo -e "// Java\nclass Main{public static void main(String[] args){System.out.println(\"Hello $date\");}}" > "${file}.java"
            ;;
        r)
            echo -e "# R\nprint('Hello $date')" > "${file}.r"
            ;;
    esac

    git add .
    git commit -m "auto: $lang update $date"

    sleep $((RANDOM % 60))
done

git push origin main