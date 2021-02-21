<?xml version = "1.0" encoding = "UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="//data">
        <html>
            <head>
                <title>XHTML for Task Four</title>
                <style type="text/css">
                    .flex-wrapper {
                        display: flex;
                        flex-direction:column;
                        align-items: center;
                        background-color: #e3fff6;
                    }

                    h2  {
                        font-size: 2em;
                        font-weight: bolder;
                        text-align: center;
                    }

                    .product {
                        display: flex;
                        align-items: center;
                        flex-direction:column;
                        margin: 2rem;
                        padding: 2rem;
                        width: 70%;
                        justify-content: space-around;
                        background-color: white;
                    }

                    img {
                        width: 400px;
                        height: 300px;
                        object-fit: contain;
                    }

                </style>
            </head>
            <body>
                <div class="flex-wrapper">

                    <xsl:for-each select="//product">
                        <div class="product">
                            <h2>
                                <xsl:value-of select="./title"/>
                            </h2>
                            <img>
                                <xsl:attribute name="src">
                                    <xsl:value-of select="./image"/>
                                </xsl:attribute>
                            </img>
                            <p>
                                <xsl:value-of select="./description"/>
                            </p>
                        </div>
                    </xsl:for-each>

                </div>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>