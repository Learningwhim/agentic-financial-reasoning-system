from app.orchestration.pipeline import app

from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule

console = Console()

console.print(
    Rule("[bold cyan]AI INVESTMENT ANALYSIS SYSTEM[/bold cyan]")
)

result = app.invoke({
        "query": "Should I invest in NVIDIA?"
    })

# QUERY
console.print(
    Panel(
        result["query"],
        title="[bold yellow]QUERY[/bold yellow]",
        border_style="yellow"
    )
)

# BULL CASE
bull_text = f"""
            [green]Score:[/green] {result["bull_case"]["score"]}/10
            [green]Confidence:[/green] {result["bull_case"]["confidence"]}

            [bold]Reasoning:[/bold]

            {result["bull_case"]["reasoning"]}
            """

console.print(
    Panel(
        bull_text,
        title="[bold green]BULL ANALYSIS[/bold green]",
        border_style="green"
    )
)

# BEAR CASE
bear_text = f"""
            [red]Score:[/red] {result["bear_case"]["score"]}/10
            [red]Confidence:[/red] {result["bear_case"]["confidence"]}

            [bold]Reasoning:[/bold]

            {result["bear_case"]["reasoning"]}
            """

console.print(
    Panel(
        bear_text,
        title="[bold red]BEAR ANALYSIS[/bold red]",
        border_style="red"
    )
)

# CRITIQUE
critique_text = f"""
                [yellow]Risk Level:[/yellow] {result["critique"]["risk_level"]}
                [yellow]Confidence:[/yellow] {result["critique"]["confidence"]}

                [bold]Final Reasoning:[/bold]

                {result["critique"]["final_reasoning"]}
                """

console.print(
    Panel(
        critique_text,
        title="[bold magenta]CRITIC EVALUATION[/bold magenta]",
        border_style="magenta"
    )
)

# FINAL DECISION
console.print(
    Panel(
        f"[bold white]{result['final_decision']}[/bold white]",
        title="[bold cyan]FINAL DECISION[/bold cyan]",
        border_style="cyan"
    )
)

console.print(
    Rule("[bold green]PIPELINE EXECUTION COMPLETE[/bold green]")
)