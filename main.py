import func
import face
import nvapi


# func.face("이미지 주소")

# 함수 호출
# face.face_func('https://th.bing.com/th/id/OIP.z7FZemly-c7BLFlHdSwLCwHaLH?w=182&h=273&c=7&r=0&o=5&dpr=1.25&pid=1.7')

news = nvapi.news('불금')
print(news) # nvapi.new에서 전달된 데이터를 출력