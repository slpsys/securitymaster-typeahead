(function ($){
	$('.typeahead').typeahead({
 		name: 'security-master',
  		prefetch: 'data/symbols.json', 
  		template: [
  			'<span class="master-symbol">{{symbol}}</span>',                              
  			' — ',
    		'<span class="master-name">{{name}}</span>', 
  		].join(''),
  		engine: Hogan,
  		limit: 10
	});
})(window.jQuery);
