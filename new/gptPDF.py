import PyPDF2
import openai, tiktoken
import os, time

openai.api_key = os.getenv("GPT_KEY")

def getPDFmes(pdf_file_path):
    pages_text = []
    pdf_file = open(pdf_file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page_num in range(len(pdf_reader.pages)):
        page_text = pdf_reader.pages[page_num].extract_text().lower()
        pages_text.append(page_text)
    
    return pages_text

def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613"):
  """Returns the number of tokens used by a list of messages."""
  try:
      encoding = tiktoken.encoding_for_model(model)
  except KeyError:
      encoding = tiktoken.get_encoding("cl100k_base")
  if model == "gpt-3.5-turbo-0613":  # note: future models may deviate from this
      num_tokens = 0
      for message in messages:
          num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
          for key, value in message.items():
              num_tokens += len(encoding.encode(value))
              if key == "name":  # if there's a name, the role is omitted
                  num_tokens += -1  # role is always required and always 1 token
      num_tokens += 2  # every reply is primed with <im_start>assistant
      return num_tokens
  else:
      raise NotImplementedError(f"""num_tokens_from_messages() is not presently implemented for model {model}.
  See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.""")


def sendToOpenai(pdf:list,
                question:str):
    response = {}
    startPage = 1
    tmpPageInfo = ""
    pageInfo = ""
    for pageNum in range(len(pdf)):
        tmpPageInfo += pdf[pageNum]
        checkSendMes = [{"role": "user", "content": f"{question}:{tmpPageInfo}"}]
        checkToken = num_tokens_from_messages(checkSendMes)
        if checkToken >= 3600:    # 若大于3600则发送一批数据
            toSendMes = [{"role": "user", "content": f"{question}:{pageInfo}"}]
            completions = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0613",
                messages=toSendMes
            )
            pageInfo = pdf[pageNum]
            tmpPageInfo = pdf[pageNum]
            response[f"page{startPage}-{pageNum}"] = completions.choices[0].message.content
            startPage = pageNum+1
            time.sleep(5)

            if pageNum == len(pdf)-1:
                toSendMes = [{"role": "user", "content": f"{question}:{pageInfo}"}]
                completions = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo-0613",
                    messages=toSendMes
                )
                response[f"page{startPage}-{pageNum+1}"] = completions.choices[0].message.content
        else:
            pageInfo += pdf[pageNum]
            
            if pageNum == len(pdf)-1:
                toSendMes = [{"role": "user", "content": f"{question}:{pageInfo}"}]
                completions = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo-0613",
                    messages=toSendMes
                )
                response[f"page{startPage}-{pageNum+1}"] = completions.choices[0].message.content
    
    return response


if __name__ == "__main__":
    pdfmes = getPDFmes("Valsson, Parrinello - 2013 - Thermodynamical Description of a Quasi-First-Order Phase Transition from the Well-Tempered Ensemble.pdf")
    # mes = [{"role": "user", "content": f"{'总结以下文字'}:{[pdfmes]}"}]
    # a = num_tokens_from_messages(mes)
    # print(a)
    b = sendToOpenai(pdfmes, "总结以下文字")
    print(b)

    