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

    .margin {
        height: 20pt;
    }

    .label.small td {
        border-top: 0.02cm dashed #000000;
        border-bottom: 0.02cm dashed #000000;
    }

    .label.small td.left {
        border-left: 0.02cm dashed #000000;
    }

    .label.small td.right {
        border-right: 0.02cm dashed #000000;
    }

    .label.small .label-name,
    .label.small .label-description {
        padding-left: 6pt;
        line-height: 10pt;
        font-size: 12pt;
        line-height: 16pt;
    }

    .label.small .label-name  {
        font-family: "Open Sans Bold";
    }

    .label.small .label-image  {
        line-height: 0pt;
        font-size: 0pt;
        vertical-align: middle;
        padding-right: 6pt;
    }
</style>
