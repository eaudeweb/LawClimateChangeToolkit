function changePage(item, page_number) {
    var pdf_page = item.attr('data').replace(/#page=\d+/, '#page='+page_number)
    item.attr("data", pdf_page);
}

$(document).ready(function(){


  $('#top-header .right-div').addClass('manage-left-header');
  $('.footer-section').remove();

  var AjaxSubmit = {};
  var law_id = parseInt($("#law_pk").val());
  var page_number = parseInt($("#page_number").text());
  var pages = null;

  $.ajax({
    dataType: "json",
    url: '/legislation/' + law_id + '/pages',
    async: false,
    success: function(data) {
      pages = data;
    }
  });

  $('#addArticle').validate({});

  var input_law_id = $("<input>")
                 .attr("type", "hidden")
                 .attr("name", "law_id").val(AjaxSubmit["law_id"]);
  var input_page = $("<input>")
                 .attr("type", "hidden")
                 .attr("id", "form_page_id")
                 .attr("name", "page").val(page_number);
  var input_article = $("<input>")
                 .attr("type", "hidden")
                 .attr("name", "article_id").val(parseInt($("#article_pk").val()));
  $('#addArticle').append($(input_law_id));
  $('#addArticle').append($(input_page));
  $('#editArticle').append($(input_article));
  $('#editArticle').append($(input_law_id));

  $max_page = Object.keys(pages).length;
  document.getElementById("raw-text-page").innerHTML = pages[$("#starting_page").val()];

  $("#prev").on('click', function(){
    page_number = page_number - 1;
    $("#raw-text-page").html(pages[page_number]);
    $("#page_number").html(page_number);
    $("#id_page").val(page_number);
    $("#form_page_id").val(page_number);
    changePage($('.pdf'), page_number)
    $("#next").prop("disabled", false);
    if( page_number == 1)
      $("#prev").prop("disabled", true);
    else
      $("#prev").prop("disabled", false);
  });

  $("#next").on('click', function(){
    page_number = page_number + 1;
    $("#raw-text-page").html(pages[page_number]);
    $("#page_number").html(page_number);
    $("#id_page").val(page_number);
    $("#form_page_id").val(page_number);
    changePage($('.pdf'), page_number)
    $("#prev").prop("disabled", false);
    if( page_number == $max_page)
      $("#next").prop("disabled", true);
    else
      $("#next").prop("disabled", false);
  });

  $("body").on('click','#save-and-continue-btn', function(){
    if ($("#addArticle").valid()) {
      $page_number = parseInt($('#page_number').text());
      AjaxSubmit["page_number"] = $page_number;
      AjaxSubmit["code"] = $("#id_code").val();
      AjaxSubmit["legislation_text"] = $("#id_text").val();
      AjaxSubmit["page"] = $("#id_page").val();
      AjaxSubmit["csrfmiddlewaretoken"] = $("[name=csrfmiddlewaretoken]").val()
      AjaxSubmit["save-and-continue-btn"] = "";
      $('input:checkbox:checked').each(function(){
        AjaxSubmit[$(this).attr("name")] = 'on';
      });
      var law_id = parseInt($("#law_pk").val());
      $.ajax({
        type: 'POST',
        url: '/legislation/' + law_id + '/articles/add/',
        data: AjaxSubmit,
        success : function(data) {
          $page_container_half = $(data).find('.page-container').html();
          $(".page-container").html('').append($page_container_half);
        }
      });
    }
  });

 });
