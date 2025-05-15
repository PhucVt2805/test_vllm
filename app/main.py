import os
import openai

vllm_api_base = os.getenv("VLLM_API_BASE", "http://localhost:8000/v1")
vllm_api_key = os.getenv("VLLM_API_KEY", "EMPTY")

client = openai.OpenAI(
    api_key=vllm_api_key,
    base_url=vllm_api_base,
)
model_name = "Qwen/Qwen2.5-Coder-0.5B-Instruct"

try:
    completion = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "Bạn là một trợ lý AI hữu ích."},
            {"role": "user", "content": "Hãy kể 1 câu chuyện thú vị"},
        ],
        max_tokens=32700,
        temperature=0.7,
    )
    print("Phản hồi từ vLLM:")
    print(completion.choices[0].message.content)

except openai.APIConnectionError as e:
    print(f"Lỗi kết nối tới vLLM: {e}")
    print("Đảm bảo dịch vụ vLLM đang chạy và có thể truy cập từ client_service.")
except openai.RateLimitError as e:
    print(f"Lỗi Rate Limit (không mong đợi với vLLM): {e}")
except openai.APIStatusError as e:
    print(f"Lỗi trạng thái API từ vLLM: {e.status_code}")
    print(f"Response: {e.response.text}")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")