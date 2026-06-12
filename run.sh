#!/bin/bash
# https://www.gnu.org/software/bash/manual/bash.html#Case-Conditionals - вот здесь прочитала про то, какой синтаксис у case (можно по поиску на странице достаточно быстро найти)

case "$1" in 
    build_generator)
        echo "Собран образ для контейнера генератора"
        docker build -t generator ./generate
        ;;
    run_generator)
        echo "Запущен контейнер"
        mkdir -p data
        docker run --rm -v "$(pwd)/data:/data" generator
        echo "Контейнер сгенерирован локально: data/data.csv"
        ;;
    create_local_data)
        echo "Запуск генератора для локальной отладки"
        mkdir -p local_data
        python3 generate/generate.py local_data
        echo "Создан local_data/data.csv"
        ;;
    *)
        echo "Использование: ./run.sh {build_generator|run_generator|create_local_data}"
        exit 1
        ;;
esac