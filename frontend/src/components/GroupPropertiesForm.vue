<template>
    <div>
        <v-text-field v-model="group.name" label="Gruppenname"></v-text-field>
          <v-text-field v-model="group.description" label="Beschreibung"></v-text-field>
          <v-text-field v-model="group.organization" label="Organisation"></v-text-field>


          Bearbeitungsrechte:
          Mitglieder
          <v-switch v-model="group.settings.membersCreate" label="können Sammlungen erstellen"></v-switch>
          Jeder:
          <v-switch v-model="group.settings.pub" label="kann Grupe sehen"></v-switch>

          <v-switch v-model="group.settings.allCreate" label="kann Sammlungen erstellen" :disabled="!group.settings.pub"></v-switch>

          Beitreten:
          <v-switch v-model="group.settings.needPassword" label="Zum Beitreten wird ein Passwort benötigt"></v-switch>
          <v-text-field v-model="group.settings.password" label="Passwort" :disabled="!group.settings.needPassword"></v-text-field>

    </div>
</template>

<script>
export default {
    props:['group']
}
</script>