
        function getId() {
        const inputElement = document.getElementById("id_photo");
        button = document.getElementById('button_img');
        inputElement.addEventListener("change", handleFiles, false);
        function handleFiles(e) {
            const fileList = this.files;
            var fileName = '';
            if(fileList){
                 fileName = fileList.item(0).name;
                 button.value += fileName;
                 inputElement.style.display = "none";
            }else{
            button.value='What is it?';
            }
        }
}







