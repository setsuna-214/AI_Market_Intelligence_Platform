from datetime import datetime
from pathlib import Path


class ReportGenerator:


    def __init__(self, output_path):

        self.output_path = Path(output_path)



    def generate(self, analysis_result):

        report = []


        report.append(
            "# China E-commerce Market Intelligence Report\n"
        )


        report.append(
            f"Date: {datetime.now().date()}\n"
        )


        # Overview

        report.append(
            "## Overview\n"
        )


        report.append(
            f"Total news collected: "
            f"{analysis_result['total_articles']}\n"
        )



        # Companies

        report.append(
            "\n## Company Exposure\n"
        )


        companies = analysis_result.get(
            "companies",
            {}
        )


        if companies:

            report.append(
                "| Company | Mentions |\n"
            )

            report.append(
                "|---|---:|\n"
            )


            for company, count in sorted(
                companies.items(),
                key=lambda x: x[1],
                reverse=True
            ):

                report.append(
                    f"| {company} | {count} |\n"
                )

        else:

            report.append(
                "No companies identified.\n"
            )



        # Topics

        report.append(
            "\n## Key Topics\n"
        )


        topics = analysis_result.get(
            "topics",
            {}
        )


        if topics:

            report.append(
                "| Topic | Mentions |\n"
            )

            report.append(
                "|---|---:|\n"
            )


            for topic, count in sorted(
                topics.items(),
                key=lambda x:x[1],
                reverse=True
            ):

                report.append(
                    f"| {topic} | {count} |\n"
                )


        else:

            report.append(
                "No topics identified.\n"
            )



        # Sources

        report.append(
            "\n## Sources\n"
        )


        for source, count in analysis_result["sources"].items():

            report.append(
                f"- {source}: {count}\n"
            )



        # Categories

        report.append(
            "\n## Categories\n"
        )


        for category, count in analysis_result["categories"].items():

            report.append(
                f"- {category}: {count}\n"
            )



        self.output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        with open(
            self.output_path,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(
                "\n".join(report)
            )