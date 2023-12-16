from flask import Flask, render_template

app = Flask(__name__)

# 个人信息
personal_info = {
    'name': 'xiaoyutianL',
    'birth_year': '1990',
    'birth_month': '01',
    'email': 'zhangsan@example.com',
    'phone': '13800138000',
    'native_place': '成都'
}

# 教育经历
education_experience = [
    {'school': '高中', 'year': '2013-2016'},
    {'school': '大学', 'year': '2016-2020'}
]

# 工作经历
work_experience = [
    {'company': '公司A', 'position': '业务员（见习）', 'year': '2020-2021'},
    {'company': '公司B', 'position': '业务员', 'year': '2021-至今'}
]

# 奖惩情况
awards_rewards = [
    {'type': '奖励', 'content': '获得优秀学生奖'},
    {'type': '奖励', 'content': '获得最佳员工奖'}
]

# 技能证书
skills_certificates = [
    {'name': '普通话二甲', 'year': '2010'},
    {'name': '驾驶证', 'year': '2015'}
]

@app.route('/')
def index():
    return render_template('resume.html', personal_info=personal_info, education_experience=education_experience, work_experience=work_experience, awards_rewards=awards_rewards, skills_certificates=skills_certificates)

if __name__ == '__main__':
    app.run(debug=True)
