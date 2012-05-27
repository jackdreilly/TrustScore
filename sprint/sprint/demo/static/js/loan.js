function statsCallback(data) {
	var list = $('<dl class="dl-horizontal">');
	var labels = ["Credit Score","Endorsers' Scores", "Endorser Factor", "Evaluation Score", "Threshold"];
	var values = [data.cs, data.e_scores, data.e_score, data.tot_score, data.threshold];
	
	$('#evaluate')
}
$("#evaluate-button").click( function (e) {
	Dajaxice.trust.trust_stats(statsCallback, {'loan_pk': pk});
});

$(".endorser-row").popover({
	'placement': 'left'
});
