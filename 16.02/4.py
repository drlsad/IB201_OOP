class Report:
    def render(self, data) -> str:
        header = self._format_header()
        body = self._format_body(data)
        footer = self._format_footer()
        return header + body + footer

    def _format_header(self) -> str:
        raise NotImplementedError()

    def _format_body(self, data) -> str:
        raise NotImplementedError()

    def _format_footer(self) -> str:
        raise NotImplementedError()



class HtmlReport(Report):
    def _format_header(self) -> str:
        return "<html><h1>Report</h1>"

    def _format_body(self, data) -> str:
        items = ''.join(f"<li>{item}</li>" for item in data)
        return f"<ul>{items}</ul>"

    def _format_footer(self) -> str:
        return "<p>End</p></html>"


r = HtmlReport()
print(r.render(["A", "B"]))


