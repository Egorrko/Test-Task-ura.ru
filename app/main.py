import typer

from fizzbuzz import fizzbuzz

app = typer.Typer(add_completion=False)


@app.command()
def main(min: int = 1, max: int = 15):
    for i in fizzbuzz.generator(min=min, max=max):
        typer.echo(i)


if __name__ == '__main__':
    app()
