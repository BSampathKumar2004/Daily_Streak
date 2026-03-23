#!/bin/bash

# Move to repo
cd /home/criativo/Documents/Coding/Daily_Streak_GitHub/Daily_Streak || exit

# Fix PATH for cron
export PATH=/usr/bin:/bin:/usr/local/bin

# Random commits count (5 to 10)
count=$((RANDOM % 6 + 5))

for ((i=1; i<=count; i++))
do
    date=$(date +"%Y-%m-%d %H:%M:%S")

    # Random language
    langs=("py" "c" "cpp" "java" "r")
    lang=${langs[$RANDOM % ${#langs[@]}]}

    file="code_${i}_$(date +%s).$lang"

    case $lang in
        py)
            echo -e "# Python\nprint('Hello $date')" > $file
            ;;
        c)
            echo -e "// C\n#include <stdio.h>\nint main(){printf(\"Hello $date\");}" > $file
            ;;
        cpp)
            echo -e "// C++\n#include <iostream>\nint main(){std::cout<<\"Hello $date\";}" > $file
            ;;
        java)
            echo -e "// Java\nclass Main{public static void main(String[] args){System.out.println(\"Hello $date\");}}" > $file
            ;;
        r)
            echo -e "# R\nprint('Hello $date')" > $file
            ;;
    esac

    git add .
    git commit -m "auto: $lang update $date"

    # small delay (avoid spam pattern)
    sleep $((RANDOM % 60))
done

git push origin main