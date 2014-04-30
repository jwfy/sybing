!function(){
	$(".sidebar-item-show").click(function(){
		$oo = $(this).parent().nextAll()
		$oo.slideDown()
		$(this).removeClass().addClass("sidebar-item-hide")
		$(this).html("收缩");
	});
	
	$(".sidebar-item-hide").click(function(){
		//  现在开始针对 其他的元素开始进行操作
	    $oo = $(this).parent().nextAll()
		//console.log($oo.length)
		$oo.slideUp()
		$(this).removeClass().addClass("sidebar-item-show")
		$(this).html("展开");
	});
}();