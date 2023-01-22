import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf
import warnings
import rich
from rich.prompt import Prompt
import errno
from rich.console import Console
console = Console()

warnings.filterwarnings(
    "ignore", category=UserWarning, module="transformers.generation_utils"
)
warnings.filterwarnings("ignore", category=UserWarning, module="requests")

from transformers import T5Tokenizer, T5ForConditionalGeneration


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


mkdir_p("./weights")

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-xl")
model = T5ForConditionalGeneration.from_pretrained(
    "google/flan-t5-xl", device_map="auto", offload_folder="./weights"
)


if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

while True:
    print()
    input_text = Prompt.ask("[bold yellow]Enter your question: [/bold yellow]")
    print()
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids

    tf.random.set_seed(0)

    sample_outputs = model.generate(
        input_ids,
        do_sample=True,
        max_length=150,
        top_k=50,
        top_p=0.95,
        num_return_sequences=7,
    )

    for i, sample_output in enumerate(sample_outputs):
        console.print(
            "{}: {}".format(
                i, tokenizer.decode(sample_output, skip_special_tokens=True)
            ),
            style="dodger_blue2",
        )
