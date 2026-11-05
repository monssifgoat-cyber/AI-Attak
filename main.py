"""الخط الرئيسي: يمرّ بالمراحل حسب config.yaml"""
import yaml, json, argparse, os
from rich.console import Console
from core.llm import LLM
from core.agents import ReconAgent, ScannerAgent, ExploiterAgent, ReporterAgent
console = Console()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config.yaml")
    args = ap.parse_args()
    cfg = yaml.safe_load(open(args.config, encoding="utf-8"))
    llm = LLM(cfg["llm"])
    target = cfg["scope"]["targets"][0]

    context = {}
    if cfg["stages"]["recon"]:
        context["recon"] = ReconAgent("Recon", llm).run(target, cfg)
    if cfg["stages"]["scan"]:
        context["scan"] = ScannerAgent("Scanner", llm).run(target, cfg)
    if cfg["stages"]["exploit"]:
        context["exploit"] = ExploiterAgent("Exploiter", llm).run(target, context.get("scan", {}), cfg)
    if cfg["stages"]["report"]:
        report = ReporterAgent("Reporter", llm).run(target, context)
        with open("reports/report.json", "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        console.print("[bold green]✔ التقرير جاهز: reports/report.json[/]")

if __name__ == "__main__":
    main()
