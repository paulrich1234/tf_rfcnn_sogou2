import os
import time
import cap6
import urllib
from flask import Flask
from flask import request
import shutil

app = Flask(__name__)
PATH_SIX='data/demo/'


@app.route('/seccode.jpg', methods=['POST', 'GET'])
def VerificationCodeNature():
    path = request.form['imageurl']
    print(path)
    answer_key = get_idenfy_code_Natrue(path)
    return answer_key

def get_idenfy_code_Natrue(url):
      global PATH
      ts_start = time.time()
      urllib.urlretrieve(url, PATH_SIX + 'ts6.jpg')
      # shutil.copy(PATH + 'ts.jpg', 'data/' + str(ts_start) + 'ts.jpg')
      print('download pic6 success')
      file_name = 'ts6.jpg.csv'
      if os.listdir(PATH_SIX) is not None:
          os.system('python list.py')
          os.system('python data/resize.py')
          os.system('sh run2')
          answer_key = cap6.get_result(file_name)
          ts_end = time.time()
          print(ts_end - ts_start)

      # os.remove(PATH_SIX + 'ts6.jpg')
      return answer_key


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)