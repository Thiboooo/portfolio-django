// Lightbox

function afficher_image(index){
    var longueur = galerie.getElementsByTagName("a").length;
    var images = $("a[rel='zoom']");
    var taille = index+1;

    if(index<0){index=longueur-1;taille=longueur}
    else if(index>longueur-1){index=0;taille=1}

    $(".voile").fadeIn();
    $(".lightbox").fadeIn();
    
    $(".lightbox").html(
        "<img src='"+images[index]+"'>" +
        "<div id='croix'></div>" +
        "<a class='fleches' id='left' onclick='afficher_image("+(index-1)+")'>←</a>" +
        "<p class='texte'>"+$(images[index]).attr("alt")+"</p>" +
        "<a class='fleches' id='right' onclick='afficher_image("+(index+1)+")'>→</a>" +
        "<p class='texte' id='right'>"+taille+"/"+longueur+"</p>"
    );

    croix.onclick = function(){
        $(".voile").fadeOut();
        $(".lightbox").fadeOut();
    };
}

$(document).ready(function(){

    $("a[rel='zoom']").click(function(e){
        e.stopPropagation();
        e.preventDefault();

        var index = $(this).index();

        $(".lightbox").html(
            afficher_image(index)
        );
    });

     // Précédent - Suivant avec les touches
    $(document).keydown(function(key) {
        switch(parseInt(key.which,10)) {
            case 37:$("#left").click();
            break;
            case 39:$("a#right").click();
            break;
        }
    });

    // Fermeture de la lightbox avec la touche échap (27)
    $(document).keydown(function(key) {
        switch(parseInt(key.which,10)) {
            case 27:
                $(".voile").fadeOut();
                $(".lightbox").fadeOut();
            break;
        }
    });

    $(".voile").click(function(){
        $(".voile").fadeOut();
        $(".lightbox").fadeOut();
    });
});