<template lang="">
    <div>
        <form @submit="onSubmit">
            <div>
                <label>Nombre</label>
                <br>
                <input type="text" name="nombre" v-model="nombre" placeholder="Nombre">
                <br>
            </div>
            <div>
                <br>
                <label for="">Edad</label>
                <br>
                <input type="number" v-model="edad" name="edad" id="">
            </div>
            <input type="submit" value="">
        </form>
    </div>
</template>

<script>

export default {
    name:"AddUser",
    data() {
        return {
            nombre: "",
            edad: ""
        }
    },
    methods: {
        onSubmit(e) {
            e.preventDefault()
            const newUser = {
                nombre: this.nombre,
                edad: this.edad
            }

            this.$emit('add-user', newUser)

            this.nombre = ""
            this.edad = ""
        }
    },
}

</script>

<style lang="">
    
</style>