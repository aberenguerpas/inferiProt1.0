
<script setup>
    import { onMounted, ref } from 'vue';
 
    const url = ref()

    onMounted(()=>{
        url.value = window.location.href;
        console.log(url.value)
    })


</script>


<template>
  <div class="lg:w-6/12 w-full py-8 mx-auto flex ">
    
    <div class="w-3/12 mx auto">
      <div class="icon bg-[#55acee] mx-auto">
        <a
          class="fa fa-twitter fa-lg"
          :href="`https://twitter.com/intent/tweet?url=${url}`"
        ></a>
      </div>
    </div>
    <div class="w-3/12 mx-auto">
      <div class="icon bg-[#3b5998] mx-auto">
        <a
          class="fa-brands fa-facebook"
          href="https://www.facebook.com/sharer/sharer.php?u=http%3A%2F%2Finferia.io%2FuseCases%2Fbonoconsumo&amp;src=sdkpreparse"
        ></a>
      </div>
    </div>
    
    <div class="w-3/12 mx-auto">
      <div class="icon bg-[#25D366] mx-auto">
        <a
          class="fa-brands fa-whatsapp fa-lg"
          :href="`https://api.whatsapp.com/send?text=${url}`"
        ></a>
      </div>
    </div>

    <div class="w-3/12 mx-auto">
      <div class="icon bg-[#3b5998] mx-auto">
        <a
          class="fa-brands fa-lg fa-linkedin fa-lg"
          :href="`https://www.linkedin.com/sharing/share-offsite/?url=${url}`"

        ></a>
      </div>
    </div>
    
  </div>
</template>

<style scoped>
.icon {
  border-radius: 50%;
  height: 50px;
  width: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
}

a{
    color: white;
    background-color: transparent;
}

a:hover{
  background-color: transparent;;
  color: black;
}
</style>
