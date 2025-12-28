#تستخدم بايثون لتطوير الويب لدينا نوعين من اطر العمل هما :django , flask
#flask:سنتعرف على
#اولا نثبت في التيرمنال virtualenv
#بالامر: pip install virtualenv لعزل مكتبات المشارع كل مشروع له مكتبة خاصة به
#للتحقق من تثبيته في التيرمنال نكتب : virtualenv --version
#ننشئ البيئة الافتراضية ل فلاسك:
#cd day26#ندخل على مجلد المشروع
#python -m venv venv  انشاء البيئة الافتراضية ط1
#virtualenv venv#ط2
#venv\Scripts\activate#تفعيل البئة الافتراضية
#where python
#python -c "import sys; print(sys.executable)"
#pip install flask#تثبيت فلاسك
#pip freeze#التحقق من لتثبيتات
# python app.py#نشغل التطبيق
'''from flask import Flask#استيراد Flask
import os#استيراد os
app=Flask(__name__)#إنشاء تطبيق Flask
@app.route('/')
def home():#دالة الصفحة الرئيسية
    return "<h1>welcome</h1>"
@app.route('/about')
def about():#دالة صفحة ثانية
    return "<h1>About</h1>"
if __name__ == '__main__':#شغّل التطبيق فقط إذا هذا الملف هو الملف الرئيسي
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
#الخطوة التالية:نعرض ملف HTML بدل نص باستخدام render_template
#داخل day26 ننشئ مجلد قوالب اسمه templates
#داخل مجلد templates: ننشئ ملفين home.html,about.html
#جوا الدالة نرجع :return render_template('about.html او about.html')
from flask import Flask,render_template#استيراد Flask
import os#استيراد os
app=Flask(__name__)#إنشاء تطبيق Flask
@app.route('/')
def home():#دالة الصفحة الرئيسية
    return render_template("home.html")
@app.route('/about')
def about():#دالة صفحة ثانية
    return render_template("about.html")
if __name__ == '__main__':#شغّل التطبيق فقط إذا هذا الملف هو الملف الرئيسي
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)'''
#home.html:منغير العوان ل Home ومنحط بال body :welcome بخط كبير
#About.html:منغير العوان ل About ومنحط بال body :about us بخط كبير
#نكتب في body للملفين :<ul>
#  <li><a href="/">Home</a></li>
#  <li><a href="/about">About</a></li>
#</ul>
#ثم ننشئ ملف محلل نص باسم post.html نضع داخله تصميم النموذج (Form)
#يطبه هذا الملف :
from flask import Flask,request,url_for,redirect,render_template
import os
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/post',methods=['POST','GET'])
def post():
    if request.method=='POST':
        text = request.form['content']
        characters = len(text)
        words = len(text.split())
        return render_template('result.html',text=text,characters=characters,words=words)
    return render_template('post.html')
if __name__=='__main__':
    port=int(os.environ.get('PORT',5000))
    app.run(debug=True,host='0.0.0.0',port=port)
#ثم ننشئ ملف باسم layout.html قبدلا من ان نربط كل صفحة html بالملف الحالي..في هذا الملف سنختصر الامر ونجعل كل الملفات ترث منه
#إنشاء تخطيط عام layout.html لجميع الصفحات مع قائمة التنقل,
#كل شيء متكرر يذهب لملف واحد ونستخدمه لكل الصفحات،وسنربط صفحة post.html لإدخال النصوص ومعالجتها.


