from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# サンプルデータ: ユーザー情報
user_data = {
    "name": "山田 太郎",
    "contact": "yamada@example.com",
    "skills": ["Python", "データ分析", "プロジェクト管理"],
    "experience": [
        {"company": "ABC株式会社", "role": "エンジニア", "duration": "2020年〜2023年", "details": "システム開発と運用"},
        {"company": "XYZ株式会社", "role": "データサイエンティスト", "duration": "2017年〜2020年", "details": "データ分析とモデル構築"}
    ]
}

# サンプル関数: 志望動機生成
def generate_motivation(skills, company_name):
    return f"私の{', '.join(skills)}というスキルは、貴社の{company_name}で求められる要件に完全に一致していると考えています。これまで培ってきた経験を活かし、貴社の発展に貢献したいと考えています。"

# 履歴書生成API
@app.route('/generate_resume', methods=['POST'])
def generate_resume():
    data = request.json
    company_name = data.get("company_name", "御社")
    
    # 自己PRと志望動機生成
    motivation = generate_motivation(user_data["skills"], company_name)
    
    # 履歴書テンプレート
    resume = f"""
    氏名: {user_data['name']}
    連絡先: {user_data['contact']}
    
    【スキル】
    {', '.join(user_data['skills'])}
    
    【職務経歴】
    """
    for exp in user_data["experience"]:
        resume += f"\n- {exp['company']} ({exp['duration']}): {exp['role']} - {exp['details']}"
    
    resume += f"\n\n【志望動機】\n{motivation}"
    
    return jsonify({"resume": resume})

if __name__ == '__main__':
    app.run(debug=True)