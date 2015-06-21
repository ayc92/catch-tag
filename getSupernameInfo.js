/**
 * Run this script to grab all supernames and their respective woeids and bounding boxes.
 *
 * OUTPUT: supernames.json
 *
 * How to run it:
 * install node-jsdom: sudo npm install jsdom
 * run the script: node getSupernameInfo.js
 */
var jsdom = require("node-jsdom");
var fs = require("fs");

var woeidToInfo = {};
jsdom.env(
    "http://isithackday.com/geoplanet-explorer/detail.php?woeid=1&type=children",
    ["http://code.jquery.com/jquery.js"],
    function(errors, window) {
        var $ = window.$;
        $("li").each(function(idx, el) {
            var $el = $(el);
            if ($el.find('span').text() === "(Supername)") {
                // Get supername
                var supername = $el.find('a').eq(0).text();
                var $info = $el.find('ul li');
                // Get woeid
                var woeid = $info.eq(1).text().split(": ")[1];
                var $bbox = $info.eq(3);
                // Get northeast coords of bounding box
                var bboxStringNE = $bbox.find('p').eq(0).text();
                bboxStringNE = bboxStringNE.substring(3);
                var bboxNE = bboxStringNE.split(", ");
                bboxNE[0] = parseFloat(bboxNE[0]);
                bboxNE[1] = parseFloat(bboxNE[1]);
                // Get southeast coords of bounding box
                var bboxStringSE = $bbox.find('p').eq(0).text();
                bboxStringSE = bboxStringSE.substring(3);
                var bboxSE = bboxStringSE.split(", ");
                bboxSE[0] = parseFloat(bboxSE[0]);
                bboxSE[1] = parseFloat(bboxSE[1]);

                // Populate output object
                woeidToInfo[woeid] = {
                    supername: supername,
                    bbox: {
                        ne: [bboxNE[0], bboxNE[1]],
                        se: [bboxSE[0], bboxSE[1]]
                    }
                };
            }
        });
        // Write info to output json file.
        fs.writeFileSync("./supernames.json", JSON.stringify(woeidToInfo));
    }
);
