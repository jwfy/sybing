$(function(){
	var sub_status = 0;
    var form = $('.mainform');
    $("#selfpostcomment1").click(function(){
		if(sub_status){
			return false
		}
		sub_status=1;
/*        $(this).text("正在提交...");
		$.ajax({
			url:form.attr('action'),
			type:"POST",
			data:form.serialize(),
			dataType:"json",
			success: function(data){
				 if(data.status){
                     alert("成功");
                 }
                else{
                    alert("表单填写错误");
                 }
            },
			error: function(jqXHR, textStatus){
				alert(arguments[1]);
			},
            complete:function(jqXHR, textStatus){
                $(this).text("提交");
                sub_status=0;
            }
		})*/
        return false;
	});
})
