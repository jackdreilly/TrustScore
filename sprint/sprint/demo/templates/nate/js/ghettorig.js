$(document).ready(function(){

/* select tabs, hide/show .page-content */
	$('#nav-dashboard a').click(function() {
		$('.page-content').removeClass('active');
		$('#nav-main li').removeClass('active');
		$('#dashbaord').addClass('active');
		$('#nav-dashboard').addClass('active');
	});
	$('#nav-agents a').click(function() {
		$('.page-content').removeClass('active');
		$('#nav-main li').removeClass('active');
		$('#agents').addClass('active');
		$('#nav-agents').addClass('active');
	});
	$('#nav-endorsements a').click(function() {
		$('.page-content').removeClass('active');
		$('#nav-main li').removeClass('active');
		$('#endorsements').addClass('active');
		$('#nav-endorsements').addClass('active');
	});
	$('#nav-loanrequests a').click(function() {
		$('.page-content').removeClass('active');
		$('#nav-main li').removeClass('active');
		$('#loanrequests').addClass('active');
		$('#nav-loanrequests').addClass('active');
	});

});
