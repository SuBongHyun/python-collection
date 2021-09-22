#pillow module을 이용하면 파이썬에서 다양한 영상 처리를 수행할 수 있다.

#Image class 예제
from PIL import Image

# 이미지 열기
im = Image.open('python.png')
 
# 이미지 크기 출력
print(im.size)
 
# 이미지 JPG로 저장
im.save('python.jpg')

# Thumbnail 이미지 생성
size = (64, 64)
im.thumbnail(size)  

# cropping 이미지 생성(잘라내 이미지). crop(좌,상,우,하)
cropImage = im.crop((100, 100, 150, 150))
cropImage.save('python-crop.jpg')

# 이미지 크기 변환
img2 = im.resize((600, 600))
img2.save('python-600.jpg')
 
# 이미지 회전
img3 = im.rotate(90)
img3.save('python-rotate.jpg')

#이미지 필터링
blurImage = im.filter(ImageFilter.BLUR)
blurImage.save('python-blur.png')
# Other examples can be found in the references below.
#http://pythonstudy.xyz/python/article/406-파이썬-이미지-처리-Pillow
#https://blog.naver.com/PostView.nhn?blogId=heennavi1004&logNo=222061487980&from=search&redirect=Log&widgetTypeCall=true&directAccess=false
