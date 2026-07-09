import json
from pathlib import Path
from dataclasses import asdict


class JSONStorage:

    def __init__(self, path):
        self.path = Path(path)


    def save(self, articles):

        data = []

        for article in articles:
            item = asdict(article)

            # datetime无法直接json
            item["published_at"] = (
                item["published_at"].isoformat()
            )

            data.append(item)


        self.path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        with open(
            self.path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=4
            )