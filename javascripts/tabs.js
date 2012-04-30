$(document).ready(function(){
	/* This code is executed after the DOM has been completely loaded */
	
	$( "#accordion" ).accordion();
	
	/* Defining an array with the tab text and AJAX pages: */
	var Tabs = {
		'Year 1'	: 'trials/step1/nx_js_d3_graph.json',
		'Year 2'	: 'trials/step2/nx_js_d3_graph.json',
		'Year 3'	: 'trials/step3/nx_js_d3_graph.json',
		'Year 4'	: 'trials/step4/nx_js_d3_graph.json',
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
	var counter = 0;
	$.each(Tabs,function(i,j){
		counter ++;
		/* Sequentially creating the tabs and assigning a color from the array: */
		var tmp = $('<li><a href="#" class="tab '+colors[(z++%4)]+'">'+i+' <span class="left" /><span class="right" /></a></li>');
		
		/* Setting the page data for each hyperlink: */
		tmp.find('a').data('page',j).data('sidelink','y' + counter + 'link');
		
		/* Adding the tab to the UL container: */
		$('ul.tabContainer').append(tmp);
	})

	/* Caching the tabs into a variable for better performance: */
	var the_tabs = $('.tab');
	
	the_tabs.click(function(e){
		/* "this" points to the clicked tab hyperlink: */
		var element = $(this);
		
		$('#' + element.data('sidelink')).click();
		
		var powFactor = .6;
		if (element.data('sidelink') == 'y4link')
			powFactor = .45;
		
		
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
			$('#contentHolder').html('');

			var w = 700,
			    h = 500,
			    fill = d3.scale.category10();

			var vis = d3.select("#contentHolder")
			  .append("svg:svg")
			    .attr("width", w)
			    .attr("height", h);

			d3.json(element.data('page'), function(json) {
			  var force = d3.layout.force()
			      .charge(-200)
			      .linkDistance(50)
			      .nodes(json.nodes)
			      .links(json.links)
			      .size([w, h])
			      .start();

			  var link = vis.selectAll("line.link")
			      .data(json.links)
			    .enter().append("svg:line")
			      .attr("class", "link")
			      .style("stroke-width", 1.0)
			      .attr("x1", function(d) { return d.source.x; })
			      .attr("y1", function(d) { return d.source.y; })
			      .attr("x2", function(d) { return d.target.x; })
			      .attr("y2", function(d) { return d.target.y; });

			  var node = vis.selectAll("g.node")
			      .data(json.nodes)
			    .enter().append("svg:g")
			      .attr("class", "node")

			  	node.append("svg:circle")
			      .attr("r", function(d){
			      return 1.0*Math.pow(1 + parseFloat(d.name)*10, powFactor);
			      }).style("fill", function(d) { return fill(d.group); })
			        .call(force.drag);

			  vis.style("opacity", 1e-6)
			    .transition()
			      .duration(1000)
			      .style("opacity", 1);

			  force.on("tick", function() {
			    link.attr("x1", function(d) { return d.source.x; })
			        .attr("y1", function(d) { return d.source.y; })
			        .attr("x2", function(d) { return d.target.x; })
			        .attr("y2", function(d) { return d.target.y; });
    
			    node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
			  });
			});
			
		}
		else $('#contentHolder').html(element.data('cache'));
		
		e.preventDefault();
	})
	
	/* Emulating a click on the first tab so that the content area is not empty: */
	the_tabs.eq(0).click();
});
