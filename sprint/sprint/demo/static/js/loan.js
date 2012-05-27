function statsCallback(data) {
    var labels = ["Credit Score","Endorsers' Scores", "Endorser Factor", "Evaluation Score", "Threshold"];
    var values = [data.cs, data.e_scores, data.e_score, data.tot_score, data.threshold];
    var width = 500, height = 200;
	
    var x = d3.scale.linear().range([0,width]);
    var y = d3.scale.linear().range([0,height]).domain([0,d3.max([data.tot_score, data.threshold])*1.1]);

    var svg = d3.select("#evaluate-graph").append("svg")
	 .attr("width", width)
	 .attr("height",height)
	.style("padding-right", "30px")
	.style("padding-left", "30px");

    var body = svg	
	.append("g")
	.attr("transform", "translate(" + width/3 + ","  + height +   ")scale(-1,-1)")
	.attr("width", width/5);

    var labels = svg	
	.append("g")
	.attr("transform", "translate(" + width/3 + ","  + height +   ")scale(1,-1)")
	.attr("width", 4/5*width);


    body
	.append("rect")
	.attr("class","threshold")
	.attr("width",width/5*1.2)
	.attr("height",y(data.threshold))
	.attr("y", 0);

    $('.threshold').tooltip({title: "Recommended threshold for funding"});

    body
	.append("rect")
	.attr("class","cs-score")
	.attr("width",width/5)
	.attr("height",y(data.cs))
	.attr("y",0);

    $('.cs-score').tooltip({title: "Credit score value"});

    body
	.append("rect")
	.attr("class","e-score")
	.attr("width",width/5)
	.attr("height",y(data.e_score))
	.attr("y",y(data.cs));
    $('.e-score').tooltip({title: "Additional trust value gained from endorsements"});

    body.append("line")
	.attr("x1",0)
	.attr("x2",width/3)
	.attr("y1",y(data.threshold))
	.attr("y2",y(data.threshold))
	.style("stroke", "#000")
	.style("stroke-width", "5px");

    labels
	.append('g')
	.attr("transform", "translate(0," + y(data.cs) + ")")
	.append("text")
	.attr("dx", 5)
	.attr("dy",5)
	.attr("transform", "scale(1,-1)")
	.text(sprintf("Credit Score: %.0f", data.cs));
    labels
	.append('g')
	.attr("transform", "translate(0," + y(data.tot_score) + ")")
	.append("text")
	.attr("dx", 5)
	.attr("dy",5)
	.attr("transform", "scale(1,-1)")
	.text(sprintf("Endorser Score: %.0f", data.e_score));


    labels
	.append('g')
	.attr("transform", "translate(0," + y(data.threshold) + ")")
	.append("text")
	.attr("dx", 5)
	.attr("dy",5)
	.attr("transform", "scale(1,-1)")
	.text(sprintf("Funding Threshold: %.0f", data.threshold));

    if (data.tot_score >= data.threshold)
	var message = "TrustScore recommends funding this loan!";
    else
	var message = "TrustScore does not recommend funding this loan.";
    $("#evaluate-graph").append($('<div class="alert fade in" id="endorse-alert">').text(message).append('<button class="close" data-dismiss="alert">&times;</button>'));
	
}
$("#evaluate-button").click( 
    function (e) {
	Dajaxice.trust.trust_stats(statsCallback, {'loan_pk': pk});
});

