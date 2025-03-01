import os 
import ollama
from openai import OpenAI
import re
import deepl

def load_code(py_file):
    try:
        with open(f'./{py_file}.py', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"File ./{py_file}.py cannot be found.")
        return None


def code_review(model_name, code):
    # 사용할 모델과 코드 입력

    prompt = f"""
    Review this code, provide suggestions for improvement, coding best practices, 
    improve readability, and maintainability. Remove any code smells and anti-patterns. 
    Provide code examples for your suggestion. Respond in markdown format. 
    answer is in Korean.


    Code:
    {code}
    """

    # Ollama 실행
    response = ollama.chat(model=model_name, messages=[{"role": "user", "content": prompt}])

    # 결과 출력
    result = response['message']['content']
    return result

# gpt api를 이용한 번역
def translate_gpt(result, openai_api_key=None):

    client = OpenAI(api_key=openai_api_key)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "developer", "content": '''텍스트에서 포함된 파이썬 코드를 제외하고 나머지 텍스트를 한국어로 번역하세요.

    # Steps

    1. 입력된 전체 텍스트를 분석하여 파이썬 코드를 식별하세요.
    2. 코드 부분을 변형하지 않고 그대로 유지하세요.
    3. 코드가 아닌 나머지 텍스트를 한국어로 정확하게 번역하세요.
    4. 번역된 텍스트와 파이썬 코드를 원래의 순서대로 결합하여 최종 출력을 생성하세요.

    # Output Format

    번역된 텍스트와 원본 파이썬 코드(변경되지 않은 상태)를 포함한 문장 형태의 결과물을 제공하세요.

    '''},
            {
                "role": "user",
                "content": result
            }
        ]
    )

    translated_text = completion.choices[0].message.content
    return translated_text

def translate_deepl(result, deepl_api_key = None):
    
    # 코드 블록 추출
    code_blocks = re.findall(r"```python\n(.*?)\n```", result, re.DOTALL)
    
    placeholder = "__CODE_BLOCK__"
    
    # 코드 블록을 임시로 대체
    text_without_code = re.sub(r"```python\n(.*?)\n```", placeholder, result, flags=re.DOTALL)

    translator = deepl.Translator(deepl_api_key)

    # 번역
    try:
        translated_text = translator.translate_text(text_without_code, target_lang="KO").text
    except Exception as e:
        print(f"Translation failed because API usage was exceeded.: {e}")
        translated_text = text_without_code  # 번역 실패 시 원문 유지
    
    # 코드 블록 복구
    for code in code_blocks:
        translated_text = translated_text.replace(placeholder, f"```python\n{code}\n```", 1)
    
    return translated_text

def main(code_name):

    # load code
    code = load_code(code_name)

    # code review
    model_name = "deepseek-coder:6.7b-instruct"
    result = code_review(model_name, code)

    # translate text
    translated_text = translate_deepl(result)
    print(translated_text)

    # save code review
    with open(f'./{code_name}_review.md', 'w', encoding='utf-8') as f:
        f.write(translated_text)
        
    print(f"Results saved in file ./{code_name}_review.md")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")

if __name__ == '__main__':
    main('review_code')

