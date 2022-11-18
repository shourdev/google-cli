import typer
main = typer.Typer()
@main.command()
def func(text: str):
    
    typer.echo(f"https://www.google.com/search?q={text}")

if __name__ == "__main__":
    main()
