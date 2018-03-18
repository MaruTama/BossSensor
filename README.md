# 手順
画像の取得 済み  
↓  
リネーム  
["超簡単！Macで複数のファイル名を一括で変更する方法！連番付きも可能！"](https://www.danshihack.com/2014/10/20/junp/os-x-yosemite-rename.html)  
↓  
顔画像の切り出し 切り出し用のアプリを作成する  
[たくさんの画像/動画からの一部を切り抜く作業をする時に便利「Image Clipper」](https://www.moongift.jp/2011/01/20110106-3/)を入れようとしたが、エラーが出てだめだった  
そのため、[複数の画像ファイルを一括でトリミングできるMacアプリXnConvert](http://yoshichiha.com/2014/02/15/mac-app-xnconvert)で切り出しした。  
↓  
転移学習か直接モデルを作成する  
↓  
ras piに移植する。or TensorFlow Liteにしてandroidに入れてみる  

# setup
python 3.6 on pyenv
Mac High Sierra

```
#cpu版
$ pip install tensorflow
$ pip install keras
$ pip install h5py
```

ref:[macOS Sierra に pyenv + python3.5 + OpenCV3 をインストール](https://qiita.com/okaxaki/items/d9bb1efdb4360985eff8)
```
# インストール
$ brew install opencv3 --with-python3
# pythonバージョン設定
$ pyenv global 3.6.4
# ライブラリの場所確認
$ ls /usr/local/Cellar/opencv3/3.2.0/lib/
# リンクを貼る
$ ln -s /usr/local/Cellar/opencv3/3.2.0/lib/python3.6/site-packages/cv2.cpython-36m-darwin.so ~/.pyenv/versions/3.6.4/lib/python3.6/
```

# 他の顔画像のデータセットを取得する
ref:[顔画像認識に使えそうな10のデータセット](https://qiita.com/Hironsan/items/de739575cdd866226676)
Faces in the Wild をダウンロードした
```
cd ~/Downloads/
tar -zxvf faceData.tar.gz
cd faceData
mkdir jpg
# 階層構造になっているので移動する
mv ./2002/07/*/*.ppm ./jpg/
mv ./2002/08/*/*.ppm ./jpg/
mv ./2002/09/*/*.ppm ./jpg/
```

[ImageMagick installer for Mac OS X](http://cactuslab.com/imagemagick/)  
curl -O http://cactuslab.com/assets/installers/ImageMagick-6.9.1-0.pkg.zip  
zipを展開してインストールする。brew でインストールするとなぜか失敗する  

```
cd jpg/
# ImageMagickのconvertで変換する
convert *.ppm image.jpg && rm *.ppm
```

```
# 移動する
mv ./*.jpg ~/workspace/python/ProfChecker/data/other/
```

# 実行
```
# WebCameraからの認識
python camera_reader.py
# 画像からの認識
python image_reader.py
```
