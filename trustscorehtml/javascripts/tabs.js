$(document).ready(function(){
	/* This code is executed after the DOM has been completely loaded */
	
	/* Defining an array with the tab text and AJAX pages: */
	var Tabs = {
		'Tab one'	: 'trials/step1/index.html',
		'Tab two'	: 'trials/step2/index.html',
		'Tab three'	: 'trials/step3/index.html',
		'Tab four'	: 'trials/step4/index.html',
	}
	
	/* The available colors for the tabs: */
	var colors = ['blue','green','red','orange'];
	
	/* The colors of the line above the tab when it is active: */
	var topLineColor = {
		blue:'lightblue',
		green:'lightgreen',
		red:'red',
		orange:'orange'
	}
	
	/* Looping through the Tabs object: */
	var z=0;
	$.each(Tabs,function(i,j){
		/* Sequentially creating the tabs and assigning a color from the array: */
		var tmp = $('<li><a href="#" class="tab '+colors[(z++%4)]+'">'+i+' <span class="left" /><span class="right" /></a></li>');
		
		/* Setting the page data for each hyperlink: */
		tmp.find('a').data('page',j);
		
		/* Adding the tab to the UL container: */
		$('ul.tabContainer').append(tmp);
	})

	/* Caching the tabs into a variable for better performance: */
	var the_tabs = $('.tab');
	
	the_tabs.click(function(e){
		/* "this" points to the clicked tab hyperlink: */
		var element = $(this);
		
		/* If it is currently active, return false and exit: */
		if(element.find('#overLine').length) return false;
		
		/* Detecting the color of the tab (it was added to the class attribute in the loop above): */
		var bg = element.attr('class').replace('tab ','');

		/* Removing the line: */
		$('#overLine').remove();
		
		/* Creating a new line with jQuery 1.4 by passing a second parameter: */
		$('<div>',{
			id:'overLine',
			css:{
				display:'none',
				width:element.outerWidth()-2,
				background:topLineColor[bg] || 'white'
			}}).appendTo(element).fadeIn('slow');
		
		/* Checking whether the AJAX fetched page has been cached: */
		
		if(!element.data('cache'))
		{	
			/* If no cache is present, show the gif preloader and run an AJAX request: */
			$('#contentHolder').html('<img src="img/ajax_preloader.gif" width="64" height="64" class="preloader" />');

			$.get(element.data('page'),function(msg){
				$('#contentHolder').html(msg);
				
				/* After page was received, add it to the cache for the current hyperlink: */
				element.data('cache',msg);
			});
		}
		else $('#contentHolder').html(element.data('cache'));
		
		e.preventDefault();
	})
	
	/* Emulating a click on the first tab so that the content area is not empty: */
	the_tabs.eq(0).click();
});
