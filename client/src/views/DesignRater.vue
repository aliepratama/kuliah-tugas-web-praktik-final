<script>
export default {
  name: "App",
  methods : {
    async uploadDroppedFiles($event) {
        const items = $event.dataTransfer.items;
        for (let key = 0; key < items.length; key++) {
            if (items.hasOwnProperty(key)) {
            let file = items[key].webkitGetAsEntry();
            file.file(async imageFile => {

                let image = {};
                let reader = new FileReader();
                reader.onload = () => {
                image.thumbnail = reader.result;
                this.images.push(image);
                };
                reader.readAsDataURL(imageFile);
            });
            }
        }
    }
  },
  data() {
    return {
      images: []
    };
  }
};
</script>
<template>
    <div @dragover.prevent @drop.prevent="uploadDroppedFiles" class="upload-zone">
        <div class="image-container" v-for="(image, index) in images" :key="index">
            <img :src="image.thumbnail" height="150" width="150">
        </div>
    </div>
</template>
<style>
.upload-zone {
  background-color: grey;
  height: 500px;
}
</style>