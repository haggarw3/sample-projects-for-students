<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="html"/>
<xsl:template match="/">
<html>
    <head>
           <link rel="stylesheet" href="stock.css" type="text/css"></link>
    </head>
    <body>
        <div class = "header">
                <marquee behavior="scroll" direction="left" scrollamount="10">

                    <xsl:for-each select="all/ stocks">
                        <xsl:if test="change &gt; 0">
                        <font color = "#5fe83c">
                        <xsl:value-of select="ticker"/>
                            :
                        <xsl:value-of select="change"/>%
                        ......
                        </font>
                        </xsl:if>

                        <xsl:if test="change &lt; 0">
                        <font color = "#FF0000">
                        <xsl:value-of select="ticker"/>
                            :
                        <xsl:value-of select="change"/>%
                        ......
                        </font>
                        </xsl:if>
                    </xsl:for-each>
                </marquee>
        </div>

        <br></br>
        <br></br>

        <div class = "topcharts">
            <table class="winner">
                <th>
                    <center>Top Winners</center>
                </th>
                <xsl:for-each select="all/ top">
                <tr>
                    <td>
                        <xsl:value-of select="name"/>
                    </td>
                    <td>
                        <xsl:value-of select="change"/>%
                    </td>
                </tr>
            </xsl:for-each>
            </table>

            <img class ="sp" src ="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Standard_%26_Poor%27s.svg/1200px-Standard_%26_Poor%27s.svg.png"></img>
            <table class="loser">
                <th>
                    Top Losers
                </th>
                <xsl:for-each select="all/ bottom">
                <tr style ="border: 1px solid black">
                    <td>
                        <xsl:value-of select="name"/>
                    </td>
                    <td>
                        <xsl:value-of select="change"/>%
                    </td>
                </tr>
            </xsl:for-each>
            </table>
        </div>
               <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <center>
            <div>
            Want to buy some stocks? Click on any of the company images to buy shares on Robinhood
            </div>
        </center>

        <br></br>
        <br></br>


        <xsl:for-each select="all/ stocks">
        <div class="gallery">
            <a target="_blank">
            <xsl:attribute name="href">
                <xsl:value-of select="link"/>
            </xsl:attribute>

            <span class="tooltiptext">
            <img style ="border-radius: 10px">
                <xsl:attribute name="src">
                <xsl:value-of select="img_src"/>
                </xsl:attribute>
                <xsl:attribute name="height">
                    200
                </xsl:attribute>
                <xsl:attribute name="width">
                    200
                </xsl:attribute>
            </img>
            </span>
            </a>
            <div class="desc">
                <h4 class = "data"><xsl:value-of select="name"/>-<xsl:value-of select="ticker"/></h4>
                <p class = "data">Open: $<xsl:value-of select="info/open"/></p>
                <p class = "data">Close: $<xsl:value-of select="info/close"/></p>
                <p class = "data">High: $<xsl:value-of select="info/high"/></p>
                <p class = "data">Low: $<xsl:value-of select="info/low"/></p>
                <p class = "data">
                    <xsl:if test="change &gt; 0">
                        <font color = "#5fe83c">
                        <xsl:value-of select="change"/>%
                        </font>
                    </xsl:if>
                    <xsl:if test="change &lt; 0">
                        <font color = "#FF0000">
                        <xsl:value-of select="change"/>%
                        </font>
                    </xsl:if></p>
            </div>
        </div>

        </xsl:for-each>

    </body>
</html>

</xsl:template>
</xsl:stylesheet>