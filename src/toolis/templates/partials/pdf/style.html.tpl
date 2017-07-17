<style>
    @page {
        size: a4;
        @frame header {
            -pdf-frame-content: header;
            left: 40pt;
            width: 522pt;
            top: 30pt;
            height: 60pt;
        }

        @frame content {
            left: 40pt;
            width: 522pt;
            top: 100pt;
            height: 590pt;
        }

        @frame footer {
            -pdf-frame-content: footer;
            left: 40pt;
            width: 522pt;
            top: 690pt;
            height: 160pt;
        }
    }

    @page extra {
        size: a4;
        @frame header-extra {
            -pdf-frame-content: header-extra;
            left: 40pt;
            width: 522pt;
            top: 30pt;
            height: 90pt;
        }

        @frame content {
            left: 40pt;
            width: 522pt;
            top: 112pt;
            height: 578pt;
        }

        @frame footer {
            -pdf-frame-content: footer;
            left: 40pt;
            width: 522pt;
            top: 690pt;
            height: 160pt;
        }
    }

    @font-face {
        font-family: "Open Sans";
        src: url(fonts/OpenSans-Regular.ttf);
    }

    @font-face {
        font-family: "Open Sans Bold";
        src: url(fonts/OpenSans-Bold.ttf);
    }

    * {
        margin: 0pt 0pt 0pt 0pt;
    }

    body {
        font-family: "Open Sans", "Oxygen", "Times New Roman", sans-serif;
    }

    td {
        vertical-align: top;
        padding-top: 3pt;
    }

    .clear {
        clear: both;
    }

    .text-right {
        text-align: right;
    }

    .text-left {
        text-align: left;
    }

    .text-center {
        text-align: center;
    }

    .strong {
        font-family: "Open Sans Bold";
    }

    .header-title {
        font-size: 12pt;
        text-align: right;
        font-family: "Open Sans Bold";
    }

    .header-page {
        font-size: 10pt;
        text-align: right;
        font-family: "Open Sans Bold";
    }

    .table-header {
        margin-bottom: 20pt;
    }

    .table-notes {
        font-size: 10pt;
    }

    .table-notes-cell {
        padding: 0pt 4pt 0pt 4pt;
        background-color: #dddddd;
    }

    .table-notes-header {
        padding-top: 6pt;
        font-family: "Open Sans Bold";
    }

    .sender {
        font-size: 8pt;
    }

    .sender-title {
        font-family: "Open Sans Bold";
        font-size: 9pt;
    }

    .receiver {
        font-size: 8pt;
    }

    .receiver-title {
        font-family: "Open Sans Bold";
        font-size: 9pt;
    }

    .table-contents {
        line-height: 10pt;
        font-size: 8pt;
    }

    .table-contents-header {
        line-height: 4pt;
        border-bottom: 1pt solid #000000;
        font-family: "Open Sans Bold";
    }

    .table-contents-line {
        {% if config.lines %}
            border-top: 0.5pt dotted #6d6d6d;
        {% endif %}
    }

    .table-contents-cell {
        line-height: 8pt;
        padding: 2pt 0pt 2pt 0pt;
    }

    .observations-title {
        font-size: 9pt;
        font-family: "Open Sans Bold";
    }

    .observations-contents {
        font-size: 9pt;
        line-height: 16pt;
    }

    .line-footer {
        border-top: 1pt solid #000000;
        height: 0pt;
        line-height: 4pt;
        font-size: 0pt;
    }

    .table-footer {
        font-size: 9pt;
        line-height: 12pt;
    }

    .table-values-header {
        font-family: "Open Sans Bold";
    }

    .table-totals-left {
        font-family: "Open Sans Bold";
    }

    .table-totals-empty {
        line-height: 0pt;
        font-size: 0pt;
    }

    .table-totals-total {
        font-size: 12pt;
        line-height: 18pt;
        font-family: "Open Sans Bold";
    }

    .ender {
        font-size: 6pt;
        text-align: center;
    }

    .min-separator {
        line-height: 0pt;
        font-size: 0pt;
    }

    .tiny-separator {
        line-height: 4pt;
        font-size: 4pt;
    }

    .medium-separator {
        line-height: 6pt;
        font-size: 6pt;
    }

    .small-separator {
        line-height: 20pt;
    }

    .large-separator {
        line-height: 30pt;
    }
</style>
